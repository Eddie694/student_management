from django.shortcuts import render, redirect
from .models import SessionYearModel, Course, Subject, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, NotificationStudent, NotificationStaff, StudentResult
from accounts.models import Student, Staff, AdminHOD


def	admin_home (request):
    return render(request, 'hod_template/admin_home.html')

# staff session 

def	add_staff (request):
    return render(request, 'hod_template/add-staff.html')

def	manage_staff (request):
    return render(request, 'hod_template/manage-staff.html')

# Course Session
def	add_course (request):
    return render(request, 'hod_template/add-course.html')


def	manage_course (request):
    return render(request, 'hod_template/manage-course.html')

#Session Area
def	manage_session (request):
    return render(request, 'hod_template/manage-session.html')

def	add_session	(request):
    return render(request, 'hod_template/add-session.html')


#Student Session
def	add_student (request):
    return render(request, 'hod_template/add-student.html')

def	manage_student (request):
    return render(request, 'hod_template/manage-student.html')



#subject session
def	manage_subject (request):
    return render(request, 'hod_template/manage-subject.html')

def	add_subject (request):
    return render(request, 'hod_template/add-subject.html')



def	admin_staff_feedback (request):
    return render(request, 'hod_template/staff-feedback.html')

def	admin_student_feedback (request):
    return render(request, 'hod_template/student-feedback.html')


# def	add_staff_save (request):
#     return render(request, 'hod_template/add_staff_save.html')



# def	edit_staff (request):
#     return render(request, 'hod_template/edit_staff.html')

# def	edit_staff_save (request):
#     return render(request, 'hod_template/edit_staff_save.html')

# def	delete_staff (request):
#     return render(request, 'hod_template/delete_staff.html')



# def	add_course_save (request):
#     return render(request, 'hod_template/add_course_save.html')



# def	edit_course (request):
#     return render(request, 'hod_template/edit_course.html')

# def	edit_course_save (request):
#     return render(request, 'hod_template/edit_course_save.html')

# def	delete_course (request):
#     return render(request, 'hod_template/delete_course.html')



# def	add_session_save (request):
#     return render(request, 'hod_template/add_session_save.html')

# def	edit_session (request):
#     return render(request, 'hod_template/edit_session.html')

# def	edit_session_save (request):
#     return render(request, 'hod_template/edit_session_save.html')

# def	delete_session (request):
#     return render(request, 'hod_template/delete_session.html')



# def	add_student_save (request):
#     return render(request, 'hod_template/add_student_save.html')

# def	edit_student (request):
#     return render(request, 'hod_template/edit_student.html')

# def	edit_student_save (request):
#     return render(request, 'hod_template/edit_student_save.html')



# def	delete_student (request):
#     return render(request, 'hod_template/delete_student.html')



# def	add_subject_save (request):
#     return render(request, 'hod_template/add_subject_save.html')



# def	edit_subject (request):
#     return render(request, 'hod_template/edit_subject.html')

# def	edit_subject_save (request):
#     return render(request, 'hod_template/edit_subject_save.html')

# def	delete_subject (request):
#     return render(request, 'hod_template/delete_subject.html')

# def	check_email_exist (request):
#     return render(request, 'hod_template/check_email_exist.html')

# def	check_username_exist (request):
#     return render(request, 'hod_template/check_username_exist.html')

# def	student_feedback_message (request):
#     return render(request, 'hod_template/student_feedback_message.html')

# def	student_feedback_message_reply (request):
#     return render(request, 'hod_template/student_feedback_message_reply.html')

# def	staff_feedback_message (request):
#     return render(request, 'hod_template/staff_feedback_message.html')

# def	staff_feedback_message_reply (request):
#     return render(request, 'hod_template/staff_feedback_message_reply.html')

# def	student_leave_view	(request):
#     return render(request, 'hod_template/student_leave_view.html')

# def	student_leave_approve (request):
#     return render(request, 'hod_template/student_leave_approve.html')

# def	student_leave_reject  (request):
#     return render(request, 'hod_template/student_leave_reject.html')

# def	staff_leave_view (request):
#     return render(request, 'hod_template/staff_leave_view.html')

# def	staff_leave_approve (request):
#     return render(request, 'hod_template/staff_leave_approve.html')

# def	staff_leave_reject (request):
#     return render(request, 'hod_template/staff_leave_reject.html')

# def	admin_view_attendance (request):
#     return render(request, 'hod_template/admin_view_attendance.html')

# def	admin_get_attendance_dates (request):
#     return render(request, 'hod_template/admin_get_attendance_dates.html')

# def	admin_get_attendance_student (request):
#     return render(request, 'hod_template/admin_get_attendance_student.html')

# def	admin_profile (request):
#     return render(request, 'hod_template/admin_profile.html')

# def	admin_profile_update (request):
#     return render(request, 'hod_template/admin_profile_update.html')
