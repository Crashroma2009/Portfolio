from tkinter import N
from django.http import HttpResponseNotFound


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>\n Нажмите сюда ==> <a href="http://127.0.0.1:8000/">Главная страница</a> \n С уважением, администрация сайта ;)')
