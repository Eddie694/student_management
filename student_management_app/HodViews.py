from django.shortcuts import render, redirect
from .models import SessionYearModel, Course, Subject, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, NotificationStudent, NotificationStaff, StudentResult
from accounts.models import Student, Staff, AdminHOD
from django.contrib import messages
from .forms import SubjectForm, SessionForm
from accounts.models import CustomUser
from accounts.forms import AddStudentForm, AddStaffForm



def	admin_home (request):
    total_teachers = Staff.objects.all().count()
    total_students = Student.objects.all().count()
    total_courses = Course.objects.all().count()
    total_subjects = Subject.objects.all().count()
    
    
    
    contex ={
        'total_teachers':total_teachers,
        'total_students': total_students,
        'total_courses': total_courses,
        'total_subjects':total_subjects
    }
    return render(request, 'hod_template/admin_home.html', contex ) 

# staff session 

def	add_staff (request):
    if request.method == 'POST':
        form = AddStaffForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name'] 
            address=form.cleaned_data['address']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'User with this email id already exists. Please use a different email')
            elif CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'User with this username already exists. Please use a different username.')
            else:
                user = form.save()
                messages.success(request, "New staff added")
                return redirect('student_management_app:manage_staff')
    else:
        form = AddStaffForm()

    context = {
            'form': form,
        }
                   
    return render(request, 'hod_template/add-staff.html', context)

def	manage_staff (request):
    staffs = Staff.objects.all().order_by('-created_at')
    
    context={
        'staffs': staffs
    }
    return render(request, 'hod_template/manage-staff.html', context)

# Course Session
def	add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        
        new_course = Course.objects.create(course_name=course_name)
        
        messages.success(request, "New course added")
        
        return redirect('student_management_app:manage_course')
       
    
    return render(request, 'hod_template/add-course.html')


def	manage_course (request):
    courses = Course.objects.all().order_by('-created_at')
    
    context = {
        'courses': courses
    }
    
    return render(request, 'hod_template/manage-course.html' , context)

#Session Area
def	manage_session (request):
    return render(request, 'hod_template/manage-session.html')

def	add_session	(request):
    if request.method == 'POST':
        form=SessionForm(request.POST)
        if form.is_valid():
            new_session = form.save()
            
            messages.success(request, "New session added ")
            return redirect("student_management_app:manage_session")
    
    return render(request, 'hod_template/add-session.html')


#Student Session
def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'User with this email id already exists. Please use a different email')
            elif CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'User with this username already exists. Please use a different username.')
            else:
                user = form.save()
                messages.success(request, "New student added")
                return redirect('student_management_app:manage_student')
        else:
            form = AddStudentForm()

        context = {
            'form': form,
        }

        return render(request, 'hod_template/add-student.html', context)
    else:
        form = AddStudentForm()
        context = {
            'form': form,
        }

        return render(request, 'hod_template/add-student.html', context)


def	manage_student (request):
    students = Student.objects.all().order_by('-created_at')
    
    context = {
        'students':students,
    }
    
    return render(request, 'hod_template/manage-student.html', context)



#subject session
def	manage_subject (request):
    subjects = Subject.objects.all()
    
    context={
        'subjects':subjects
    }
    return render(request, 'hod_template/manage-subject.html', context)


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject_name = form.cleaned_data['subject_name']
            course_id = form.cleaned_data['course_id']  # Use the course instance directly
            staff_id = form.cleaned_data['staff_id']  # Use the staff instance directly
            
           
            course_instance = Course.objects.get(pk=course_id)
            staff_instance = CustomUser.objects.get(pk=staff_id)
            

            # Create and save the new Subject instance
            new_subject = Subject(
                subject_name=subject_name,
                course_id=course_instance,
                staff_id=staff_instance,
            )
            new_subject.save()

            messages.success(request, 'New Subject added.')
            return redirect('student_management_app:manage_subject')
    else:
        form = SubjectForm()

    return render(request, 'hod_template/add-subject.html', {'form': form})



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
