from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import  Edit_Forms, LoginForm, UserRegistrationForm
from my_site.models import Users, Resume
from personal_portfolio.settings import *

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
    data = request.POST
    edit_form = Edit_Forms(request.POST, request.FILES)
    a = request.FILES
    pk = request.user.id
    user = Users.objects.get(id=pk)

    if request.method == 'POST':
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

    context = {
        'resume_all_user': resume_all_user,
    }
    return render(request, 'my_resume.html', context)