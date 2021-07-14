from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница приложения Posts')

def group_posts(request, slug):
    return HttpResponse(f'Группа по имени {slug}')
