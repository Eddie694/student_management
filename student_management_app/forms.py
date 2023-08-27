from django import forms
from .models import Subject, Course
from accounts.models import Staff
from accounts.models import CustomUser


class SubjectForm(forms.Form):
    
    #For Displaying Courses
    try:
        courses = Course.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)  # Corrected attribute name
            course_list.append(single_course)
            print(course_list)
            
    except Course.DoesNotExist:
        print('No courses found')
        course_list = []
        
   
    
    #For Displaying list of Teachers
    try:
        staff_users = CustomUser.objects.filter(user_type=CustomUser.STAFF)  # Filter users by user type
        print(f"Number of staff users found: {staff_users.count()}")
        print(staff_users)
        staff_list = []
        
        for staff_user in staff_users:
            single_staff = (staff_user.id, f"{staff_user.first_name} {staff_user.last_name}")
            staff_list.append(single_staff)
        if not staff_list:
            print("No staff members found")
    except CustomUser.DoesNotExist:
        print("An error occurred while retrieving staff members")

    
    subject_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control' }))
    course_id = forms.ChoiceField( choices=course_list, required=True, widget = forms.Select(attrs={'class': "form-control"}))
    staff_id = forms.ChoiceField( choices = staff_list, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = Subject
        fields = ['subject_name', 'course_id', 'staff_id']
        
    
    