from django.shortcuts import render
#from django.http import HttpResponse


def home(request):
    news = [
        {
            'title' : 'Наша первая статья',
            'text' : 'Полный текст статьи',
            'date' : '1 Января 2100 года',
            'avtor' : 'Джон'
        },
        {
            'title' : 'Наша вторая статья',
            'text' : 'Полный текст статьи',
            'date' : '10 Января 2100 года',
            #теперь удалим инфу про автора
            # 'avtor' : 'Джон'
        }
    ]
    data = {
        'news': news,
        'title':'Главная страница1'
    }
    return render(request,'blog/home2.html',data)


def contacti(request):
    return render(request,'blog/contacti.html',{'title': 'Страница контакты1'})

