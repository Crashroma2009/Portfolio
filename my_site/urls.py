from django.urls import path
from my_site import views
#from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView



urlpatterns = [
    path('', views.index, name='index'),
    path('create_resume/', views.create_resume, name='create_resume'),
    path('resume_detail/<int:pk>/', views.resume_detail, name='resume_detail'),
    path('user_contacts/<int:pk>/', views.user_contacts, name='user_contacts'),
    path('search/', views.search, name='search'),
    # path('delete_of_resume/', views.delete_of_resume, name='delete_of_resume'),
    path('additional_information/', views.additional_information, name='additional_information'),
    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('account_user/', views.account_user, name='account_user'),
]

