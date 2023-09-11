from django import forms
from .models import Subject, Course, SessionYearModel
from accounts.models import Staff
from accounts.models import CustomUser


class DateInput(forms.DateInput):
    input_type = "date"


class SessionForm(forms.Form):
    session_start_year = forms.DateField(label="section start", required=True, widget=DateInput())
    session_end_year = forms.DateField(label="section start", required=True, widget=DateInput())
    
    class Meta:
        model = SessionYearModel
        
        widget = {
           'session_start_year':DateInput(),
           'session_end_year':DateInput(),
        }
    

class SubjectForm(forms.Form):
    subject_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_id = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    staff_id = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dynamically populate the course choices with (course_id, course_name) tuples
        course_choices = [(course.id, f"{course.course_name}") for course in Course.objects.all()]
        self.fields['course_id'].choices = course_choices

        # Dynamically populate the staff choices with (user_id, full_name) tuples
        staff_choices = [(staff.id, f"{staff.first_name} {staff.last_name}") for staff in CustomUser.objects.filter(user_type=CustomUser.STAFF)]
        self.fields['staff_id'].choices = staff_choices

    class Meta:
        model = Subject
        fields = ['subject_name', 'course_id', 'staff_id']
        
    
    