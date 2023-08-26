from django.shortcuts import render, redirect
from .models import SessionYearModel, Course, Subject, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, NotificationStudent, NotificationStaff, StudentResult
from accounts.models import Student, Staff, AdminHOD



def staff_home(request):

    return render(request, 'staff_template/staff_home.html')

def staff_take_attendance(request):

    return render(request, 'staff_template/staff_take_attendance.html')

def get_students(request):

    return render(request, 'staff_template/get_students.html')

def save_attendance_data(request):

    return render(request, 'staff_template/save_attendance_data.html')

def staff_update_attendance(request):

    return render(request, 'staff_template/staff_update_attendance.html')

def get_attendance_dates(request):

    return render(request, 'staff_template/get_attendance_dates.html')

def get_attendance_student(request):

    return render(request, 'staff_template/get_attendance_student.html')



def update_attendance_data(request):

    return render(request, 'staff_template/update_attendance_data.html')

def staff_apply_leave(request):

    return render(request, 'staff_template/staff_apply_leave.html')

def staff_apply_leave_save(request):

    return render(request, 'staff_template/staff_apply_leave_save.html')


def staff_feedback(request):

    return render(request, 'staff_template/staff_feedback.html')

def staff_feedback_save(request):

    return render(request, 'staff_template/staff_feedback_save.html')

def staff_profile(request):

    return render(request, 'staff_template/staff_profile.html')

def staff_profile_update(request):

    return render(request, 'staff_template/staff_profile_update.html')

def staff_add_result(request):

    return render(request, 'staff_template/staff_add_result.html')

def staff_add_result_save(request):

    return render(request, 'staff_template/staff_add_result_save.html')


