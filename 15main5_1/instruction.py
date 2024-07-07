#15main4_1
#Работа с шаблонизатором

#В Django все HTML-шаблоны должны находиться в папке templates
#создаем папку templates в blog
#теперь внутри этой папки создаем папку с названием нашего приложения
#Чтобы не было конфликтов(перезаписи одного файла templates в другой)

#создали 2 файла home.html и contacti.html
#теперь в views.py надо вместо HTML-кода прописать эти 2 шаблона
#при помощи метода render

#Выбивается ошибка:не видит шаблона blog/home.html
#Так как мы не зарегистрировали приложение blog в файле settings.py в классе INSTALLED_APPS
#через запятую вписываем 'blog'

#Возможности шаблонизатора Jinja
#Jinja - дополнительный ф-нал,кот позволяет получать данные с Back-end 
#и затем обработать в HTML


#чтобы работать с Jinja,надо в шаблоны передавать какую-либо инфу,а затем отображать в HTML

#def home(request):
    #создаем словарь
    # number = 50
    # data = {
    #     'some': number
    # }
    #теперь хотим передать эту инфу в blog/home.html
    #для этого надо передать data 3м пар-тром
    #return render(request,'blog/home.html',data)

    # теперь чтобы вывести значение some из (data):
    #  надо открыть 2 фиг. скобки и прописать,что конкретно хотим вывести
    # <p><b>{{some}}</b></p>

#дальше обьяснение в views.py и home.html

#теперь проблема с тем,что много повторяющего кода в home.html и contacti.html
#поэтому делаем шаблоны и просто меняем title

#Подключаем Bootstrap
#bootstrapcdn.com - подключение bootstrap стилей
#<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">

#https://getbootstrap.com/ - примеры 