from django.shortcuts import render
#from django.http import HttpResponse


# def home(request):
#     return HttpResponse('<h3>Привет всем</h3>')

# def contacti(request):
#     return HttpResponse('<h3>Просто страница</h3>')


#render - позволяет вывести HTML-шаблон
#return render(request,'blog/home.html') - 1й пар-тр - тот же что и в home(request)
#2й пар-тр - шаблон(пишем с учетом того что мы в папке templates - 'blog/home.html')

#чтобы работать с Jinja,надо в шаблоны передавать какую-либо инфу,а затем отображать в HTML

def home(request):
    #создаем словарь
    # number = 50
    # data = {
    #     'some': number
    # }
    #теперь хотим передать эту инфу в blog/home.html
    #для этого надо передать data 3м пар-тром

    #усложним задачу
    #создадим список,кот созтоит из словарей
    #Инфа про статьи(далее будем это все через БД)
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
    #теперь вместо ключа some подставляем news 
    #и подставляем значение список news
    data = {
        'news': news,
        #Сюда же подставляем 'title'
        'title':'Главная страница1'
    }
    return render(request,'blog/home2.html',data)


def contacti(request):
#сюда тоже можем передавать инфу,но другим способом
#также можем создавать словари без пер-ой
#и также теперь можем выводить это в contacti.html
    return render(request,'blog/contacti.html',{'title': 'Страница контакты1'})

