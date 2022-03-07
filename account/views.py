from my_site.forms import Resume_form
from personal_portfolio.settings import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
#from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from .forms import UserRegistrationForm, Edit_Forms
from my_site.models import Users, Resume
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         print(form)
#         if form.is_valid():
#             cd = form.cleaned_data
#             print(cd)
#             user = authenticate(username = cd['username'], password = cd['password'])
#             print(user)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     pk = user.id
#                     #return render('/', pk)
#                     #return HttpResponse('Авторизация прошла успешно')
#                     return redirect('user_home/', {'user': user}, {'pk':pk})
#                 else:
#                     return HttpResponse('Ошибка авторизации. Попробуйте снова')
#             else:
#                 return HttpResponse('Неверный логин')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})


# @login_required
# def dashboard(request):
#     return render(request, 'account/dashboard.html', {'section': 'dashboard'})


class User_login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    model = Users

    def get_success_url(self):
        print('Вошел')
        return reverse_lazy('user_home')


def user_logout(request):
    logout(request)
    print('Вышел')
    return redirect('login')

class Register(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    
    def get_success_url(self):
        return  reverse_lazy('login')
    

def user_home(request):    #Фун-я . Личный кабинет
    return render(request, 'user_home.html')


def edit_resume(request):     #Редактирование или добавление информации в аккаунт пользователя
    #user = Users
    data = request.POST
    #print(data)
    edit_form = Edit_Forms(request.POST, request.FILES)
    a = request.FILES
    print(a)
    pk = request.user.id
    print(pk)
    user = Users.objects.get(id=pk)
    #print(user.email)

    if request.method == 'POST':
        #data_photo = MEDIA_URL +  str(request.FILES['photo'])
        Users.objects.filter(id=pk).update(first_name=data['first_name'], last_name=data['last_name'], sity=data['sity'])
        photo = Users.objects.get(id=pk)
        photo.photo = request.FILES['photo'] 
        photo.save()      
        return redirect('user_home')
    else:
        edit_form = Edit_Forms()

    context = {
        'form': edit_form,
        'user': user,
    }
    
    return render(request, 'edit_resume.html', context)

    
    #отображение страницы резюме пользователя
def my_resume(request):
    pk = request.user.id
    resume_all_user = Resume.objects.filter(user_resume=pk)
    print(type(resume_all_user))
    for resume in resume_all_user:
        print(resume.last_name)

    context = {
        'resume_all_user': resume_all_user,
    }

    return render(request, 'my_resume.html', context)