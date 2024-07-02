from django.shortcuts import render
#сначало будем выводить обычный текст:
#для этого подключаем HttpResponse
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h3>Привет всем</h3>')

# def about(request):
#     return HttpResponse('<h3>Страница о нас</h3>')

def contacti(request):
    return HttpResponse('<h3>Просто страница</h3>')
