from django import forms
from . models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from student_management_app.models import Course, SessionYearModel
from accounts.models import Student, Staff




class RegistrationForm(UserCreationForm):
    
    USER_TYPE_CHOICES = (
        ('select User', 'Select User'),
        (CustomUser.STUDENT, 'Student'),
        (CustomUser.STAFF, 'Staff'),
        (CustomUser.HOD, 'HOD'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True,
                                  widget=forms.Select(attrs={'class': 'form-control mb-3'}))
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.',
                                            widget=forms.TextInput(attrs={'class': 'form-control '}))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.',
                                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=30, required=True, help_text='Required.',
                                            widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=30, required=True, help_text='Required.',
                                            widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['user_type', 'first_name', 'last_name', 'email','password1','password2' ]


class LoginForm(AuthenticationForm):
    USER_TYPE_CHOICES = (
        ('select User', 'Select User'),
        (CustomUser.STUDENT, 'Student'),
        (CustomUser.STAFF, 'Staff'),
        (CustomUser.HOD, 'HOD'),
    )
    
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label='User Type')






 
 
class AddStudentForm(forms.Form):
    
    email = forms.EmailField(label="Email",
                             max_length=50,
                             widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password",
                               max_length=50,
                               widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name",
                                 max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name",
                                max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username",
                               max_length=50,
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address",
                              max_length=50,
                              widget=forms.TextInput(attrs={"class":"form-control"}))
 
    #For Displaying Courses
    try:
        courses = Course.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        print("here")
        course_list = []
     
    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        print(session_years)
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year.strftime('%Y'))+" to "+str(session_year.session_end_year.strftime('%Y')))
            print(single_session_year)
            session_year_list.append(single_session_year)
            print(session_year_list)
             
    except:
        session_year_list = []
    
     
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
     
    course_id = forms.ChoiceField(label="Course",
                                  choices=course_list,
                                  widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender",
                               choices=gender_list,
                               widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year",
                                        choices=session_year_list,
                                        widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic",
                                  required=False,
                                  widget=forms.FileInput(attrs={"class":"form-control"}))
 
class AddStaffForm(forms.Form):
            
    email = forms.EmailField(label="Email",
                             max_length=50,
                             widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password",
                               max_length=50,
                               widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name",
                                 max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name",
                                max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username",
                               max_length=50,
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address",
                              max_length=50,
                              widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'password', 'address', 'username']
        
        
    def save(self):
         # Extract cleaned data from the form
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        
        # Create a new user with the provided email and password
        user = CustomUser.objects.create_user(
            username=email,  # You can use the email as the username
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            user_type=CustomUser.STAFF,
        )
        
        user.save()
        
        return user
        
class EditStaffForm(forms.ModelForm):
            
    email = forms.EmailField(label="Email",
                             max_length=50,
                             widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password",
                               max_length=50,
                               widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name",
                                 max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name",
                                max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username",
                               max_length=50,
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address",
                              max_length=50,
                              widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'address', 'username']    
         

class EditStudentForm(forms.ModelForm):
    email = forms.EmailField(label="Email",
                             max_length=50,
                             widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name",
                                 max_length=50,
                                 widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name",
                                max_length=50,
                                widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username",
                               max_length=50,
                               widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address",
                              max_length=50,
                              widget=forms.TextInput(attrs={"class":"form-control"}))
 
    # For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []
 
    # For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
             
    except:
        session_year_list = []
 
     
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
     
    course_id = forms.ChoiceField(label="Course",
                                  choices=course_list,
                                  widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender",
                               choices=gender_list,
                               widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year",
                                        choices=session_year_list,
                                        widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic",
                                  required=False,
                                  widget=forms.FileInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'address', 'username', 'session_year_id', 'gender', 'course_id', 'profile_pic'] 


