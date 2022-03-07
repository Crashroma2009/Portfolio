from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Resume, Users
from my_site.forms import *


def index(request):
    resume_form = Resume_form
    resume = Resume.objects.all()
    context = {
        'resume': resume,
        'resume_form': resume_form,
    }
    print(HttpResponse.status_code)
    return render(request, 'index.html', context)


def about(request):
    res = request.user.id   #id текущего пользователя
    print(res)
    a = request.POST
    b = request.FILES
    print(a)
    print(b)
    congratulation = 'Ваша запись успешно сохранена'
    resume_form = Resume_form(request.POST, request.FILES)
    resume_data = Resume.objects.all()
    if request.method == 'POST':
        if resume_form.is_valid():
            resume_form.save()
            pk = Resume.objects.last() #id последнего резюме
            print(pk.id)
            person = resume_data.filter(id=pk.id).update(user_resume=res)
            return redirect('index')
        else:
            resume_form = Resume_form()
    
    context = {
            'resume_form': resume_form,
            'congratulation': congratulation,
            'resume_data': resume_data,
        }
    return render(request, 'about.html', context)


#Сделать блоки try b except: 
#1) на проверку несуществующей страницыs
#2) на проверку ввода не числа, а буквы
def resume_detail(request, pk):
    resume = Resume.objects.get(id=pk)
    resume_all = Resume.objects.all()
    # load = Resume(cont_id=resume.id)
    # load.save()
    # print(resume.id)
    context = {
        'resume': resume,
        'resume_all': resume_all,
    }
    return render(request, 'resume_detail.html', context)
    #return render(request, 'index.html')


def user_contacts(request, pk):
    resume = Resume.objects.get(id=pk)
    resume_all = Resume.objects.all()
    context = {
        'resume': resume,
        'resume_all': resume_all,
        # 'contacts': contacts,
        # 'contacts_form': contacts_form,
    }
    return render(request, 'user_contacts.html', context)


def additional_information(request):
    return render(request, 'additional_information.html')


def search(request):
    model = Resume
    resume = Resume.objects.all()
    post_data = request.POST['data_']
    
    a = model.objects.filter(last_name=post_data)
    
    for i in resume:
        print(i.last_name)

    context = {
        'resume': resume,
        'post_data': post_data,
    }
    print(post_data)
    return render(request, 'search.html', context)