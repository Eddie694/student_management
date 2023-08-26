from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import CustomUser, AdminHOD, Student, Staff

# Create your views here.
def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            confirm_password = form.cleaned_data['password2']
            user_type = form.cleaned_data['user_type']
            username = email.split('@')[0].split('.')[0]

            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'User with this email id already exists. Please proceed to login!!')
            elif user_type not in [CustomUser.STAFF, CustomUser.STUDENT, CustomUser.HOD]:
                messages.error(request, "Please use a valid user type.")
            elif CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'User with this username already exists. Please use a different username.')
            else:
                user = form.save(commit=False)
                user.username = username
                user.set_password(password)
                user.save()

                messages.success(request, 'Registration successful. You can now login.')
                return redirect('accounts:login')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/registration.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}")
        print(f"Password: {password}")

        authenticated_user = authenticate(request, email=email, password=password)
        print(f"Authenticated User: {authenticated_user}")

        if authenticated_user is not None:
            login(request, authenticated_user)
            user_type = authenticated_user.user_type

            if user_type == CustomUser.HOD:
                return redirect('student_management_app:admin_home')  # Redirect for HOD user
            elif user_type == CustomUser.STAFF:
                return redirect('student_management_app:staff_home')  # Redirect for Staff user
            elif user_type == CustomUser.STUDENT:
                return redirect('student_management_app:student_home')  # Redirect for Student user
            else:
                messages.error(request, 'Invalid User Type')
        else:
            messages.error(request, 'Invalid Login Credentials')

    return render(request, 'accounts/login.html')





def logout_user(request):
    logout(request)
    return redirect('student_management_app:home')



def get_user_type_from_email(email):
    """
    Returns CustomUser.user_type corresponding to the given email address
    email_id should be in following format:
    '<username>.<staff|student|hod>@<college_domain>'
    eg.: 'abhishek.staff@jecrc.com'
    """
 
    try:
        email = email.split('@')[0]
        email_user_type = email.split('.')[1]
        return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
    except:
        return None