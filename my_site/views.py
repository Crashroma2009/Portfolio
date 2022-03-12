from cmath import exp
from django.http import HttpResponse
from django.core.exceptions import EmptyResultSet, ObjectDoesNotExist, ValidationError
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Resume, Users
from my_site.forms import *
from time import sleep

def index(request):
    resume_form = Resume_form
    resume_all = Resume.objects.all()
    context = {
        'resume_all': resume_all,
        'resume_form': resume_form,
    }
    print(HttpResponse.status_code)   #Доп.информация для разработчика
    return render(request, 'index.html', context)
   

def create_resume(request):
    """Создание нового резюме пользователя"""
    user_id = request.user.id   #id текущего пользователя
    resume_form = Resume_form(request.POST, request.FILES)
    resume_data = Resume.objects.all()
    try:
        if request.method == 'POST':
            if resume_form.is_valid():   #Если пришли правильны данные,
                resume_form.save()         # и сохраняю их
                id_last = Resume.objects.last() #Нахожу id последнего резюме, которое было создано только что и
                person = resume_data.filter(id=id_last.id).update(user_resume=user_id)  # привязываю id резюме к текущему юзеру
                return redirect('index')
            else:
                resume_form = Resume_form()
    except (AttributeError, ValidationError) as e:
        return HttpResponse(f'{e}| Форма заполнения неправильна.\n Заполните форму снова')  
    context = {
            'resume_form': resume_form,
            'resume_data': resume_data,
        }
    return render(request, 'create_resume.html', context)


def resume_detail(request, pk):
    print(request)
    try:
        resume = Resume.objects.get(id=pk)
        resume_all = Resume.objects.all()
        context = {
            'resume': resume,
            'resume_all': resume_all,
        }
    except EmptyResultSet as e:
        print(e, 'Нет результатов')
    except ObjectDoesNotExist as e:
        print(e)
    return render(request, 'resume_detail.html', context)


def user_contacts(request, pk):
    resume = Resume.objects.get(id=pk)
    resume_all = Resume.objects.all()
    context = {
        'resume': resume,
        'resume_all': resume_all,
    }
    return render(request, 'user_contacts.html', context)


def additional_information(request):
    return render(request, 'additional_information.html')


def search(request):
    model = Resume
    resume = Resume.objects.all()
    try:
        post_data = request.POST['data_']
        a = model.objects.filter(last_name=post_data)
        for i in resume:
            print(i.last_name)

        context = {
            'resume': resume,
            'post_data': post_data,
        }
        print(post_data)
    except EmptyResultSet as e:
        print(e, 'Нет результатов')
    return render(request, 'search.html', context)
    