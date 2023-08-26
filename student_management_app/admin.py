from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Course, Subject, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaff, NotificationStudent, NotificationStaff
 
# Register your models here.
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaff)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaff)

