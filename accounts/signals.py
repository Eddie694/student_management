from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, AdminHOD, Staff, Student, Course, SessionYearModel

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == CustomUser.HOD:
            AdminHOD.objects.create(admin=instance)
        elif instance.user_type == CustomUser.STAFF:
            Staff.objects.create(admin=instance)
        elif instance.user_type == CustomUser.STUDENT:
            course = Course.objects.first()  # Get a course instance (you might want to handle this better)
            session_year = SessionYearModel.objects.first()  # Get a session year instance
            Student.objects.create(
                admin=instance,
                course_id=course,
                session_year_id=session_year,
                address="",
                profile_pic="",
                gender=""
            )

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == CustomUser.HOD:
        instance.adminhod.save()
    elif instance.user_type == CustomUser.STAFF:
        instance.staff.save()
    elif instance.user_type == CustomUser.STUDENT:
        instance.student.save()
