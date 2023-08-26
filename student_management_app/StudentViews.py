from django.shortcuts import render, redirect
from .models import Course, Subject, Attendance, AttendanceReport, LeaveReportStudent, FeedBackStudent, StudentResult
from accounts.models import CustomUser, Staff, Student
from django.urls import reverse
from django.core.files.storage import FileSystemStorage



def student_home(request):

    return render(request, 'student_template/student_home.html')

def student_view_attendance_post(request):
    
    return render(request, 'student_template/student_view_attendance.html')

def student_view_attendance(request):

    return render(request, 'student_template/student_attendance.html')

def student_apply_leave(request):

    return render(request, 'student_template/student_apply_leave.html')

def student_apply_leave_save(request):

    return render(request, 'student_template/student_apply_leave_save.html')

def student_feedback(request):

    return render(request, 'student_template/student_student_feedback.html')

def student_feedback_save(request):

    return render(request, 'student_template/student_student_feedback_save.html')

def student_profile(request):

    return render(request, 'student_template/student_profile.html')
def student_profile_update(request):

    return render(request, 'student_template/student_profile_update.html')

def student_view_result(request):

    return render (request, 'student_template/student_view_results.html')