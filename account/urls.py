from django.urls import path
from . import views


urlpatterns = [
     path('login/', views.User_login.as_view(), name='login'),
     path('register/', views.Register.as_view(), name='register'),
     path('user_home/', views.user_home, name='user_home'),
     path('logout/', views.user_logout, name='logout'),
     path('edit_resume/', views.edit_resume, name='edit_resume'),
     path('my_resume/', views.my_resume, name='my_resume'),
     path('changing_user_resume/<int:pk>/', views.Changing_User_Resume.as_view(), name='Changing_User_Resume'),
]