from django.urls import path
from . import views

urlpatterns = [
    #если польз-ль перейдет на главную страницу,то обращаемся к views.py
    #и сдесь будем обращаться к опр-ой ф-ии,кот. будет показывать польз-лю
    #какую-либо информацию(нужно импортировать этот файл views.py)
    #from . import views - из той же дирректории(.) импортируем views.py
    #path('',views.home) - теперь обращаемся к views и потом к ф-ии home
    #прописываем ф-ию home в файле views.py
    path('',views.home),

    #также можем прописывать отслеживание по переходам на другие странички
    #path('about',views.about),
    
    #можем добавить сложные адреса
    path('contacti/some/123',views.contacti),
]