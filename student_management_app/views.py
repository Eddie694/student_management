from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from accounts import views

# Create your views here.

def home(request):
    
    return redirect('accounts:login')

    return render(request, 'student_management_app/home.html', {})

def contact(request):
    return render(request, 'student_management_app/contact.html')
 
