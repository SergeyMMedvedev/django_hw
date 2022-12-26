import os
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    cwd = os.getcwd()
    f_list = '<br>' + '<br>'.join(os.listdir(path=cwd))
    msg = f'Список файлов в рабочей директории: {f_list}'
    return HttpResponse(msg)
