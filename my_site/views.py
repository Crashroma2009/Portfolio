from django.http import HttpResponse
from django.core.exceptions import EmptyResultSet, ObjectDoesNotExist, ValidationError
from django.shortcuts import render, redirect
from rest_framework import generics
from django.views.generic import ListView
from my_site.models import Resume
from my_site.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from my_site.serializer import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class IndexHome(ListView):
    model = Resume
    template_name = 'index.html'
    context_object_name = 'resume_all'

# def index(request):
#     resume_form = Resume_form
#     resume_all = Resume.objects.all()
#     context = {
#         'resume_all': resume_all,
#         'resume_form': resume_form,
#     }
#     print(HttpResponse.status_code)   #Доп.информация для разработчика
#     return render(request, 'index.html', context)
   
@login_required
def create_resume(request):
    """Создание нового резюме пользователя"""
    user_id = request.user.id   #id текущего пользователя
    resume_form = Resume_form(request.POST, request.FILES)
    resume_data = Resume.objects.all()
    raise_exception = True
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
        post_data = request.POST['data_search']
        a = model.objects.filter(last_name=post_data)
        context = {
            'resume': resume,
            'post_data': post_data,
        }
    except EmptyResultSet as e:
        print(e, 'Нет результатов')
    return render(request, 'search.html', context)
    

#Here will be a view for the Portfolio app API
#Класс выдает список пользователей из БД
class ResumeAPIList(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


#Класс обновляет запись в БД
class ResumeAPIUpdate(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

#Класс удаляет запись из БД
class ResumeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = (IsAdminUser, )