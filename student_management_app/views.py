from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect


# Create your views here.

def home(request):

    return render(request, 'student_management_app/home.html', {})

def contact(request):
    return render(request, 'student_management_app/contact.html')
 
