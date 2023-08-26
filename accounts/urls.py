from django.urls import path
from .import views

app_name = 'accounts'


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('registration/', views.user_registration, name="registration"),  


]