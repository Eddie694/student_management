from django.contrib import admin
from . models import CustomUser, Student, Staff, AdminHOD
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserModelAdmin(UserAdmin):
    list_display = ['username','first_name', 'last_name', 'email', 'user_type']
    search_fields = ['first_name', 'last_name', 'email', 'user_type']
 
admin.site.register(CustomUser, CustomUserModelAdmin)

class AdminHODModelAdmin(admin.ModelAdmin):
    list_display = ['admin', 'created_at', 'updated_at']

class StaffModelAdmin(admin.ModelAdmin):
    list_display = ['admin', 'address', 'created_at', 'updated_at']

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['admin', 'gender', 'address', 'created_at', 'updated_at']

admin.site.register(AdminHOD, AdminHODModelAdmin)
admin.site.register(Staff, StaffModelAdmin)
admin.site.register(Student, StudentModelAdmin)



