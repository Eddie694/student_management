from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Course, Subject, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaff, NotificationStudent, NotificationStaff, SessionYearModel
 
# Register your models here.
class CustomCourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'created_at', 'updated_at' ]
    
admin.site.register(Course, CustomCourseAdmin)

class CustomSubjectAdmin(admin.ModelAdmin):
    list_display =['subject_name', 'course_id', 'staff_id' ,'created_at']

admin.site.register(Subject, CustomSubjectAdmin)

admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaff)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaff)
admin.site.register(SessionYearModel)

