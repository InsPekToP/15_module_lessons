from django.shortcuts import render
#from django.http import HttpResponse


# def home(request):
#     return HttpResponse('<h3>Привет всем</h3>')

# def contacti(request):
#     return HttpResponse('<h3>Просто страница</h3>')


#render - позволяет вывести HTML-шаблон
#return render(request,'blog/home.html') - 1й пар-тр - тот же что и в home(request)
#2й пар-тр - шаблон(пишем с учетом того что мы в папке templates - 'blog/home.html')

def home(request):
    return render(request,'blog/home.html')

def contacti(request):
    return render(request,'blog/contacti.html')
