#15main7_1
#Создание базы данных и и проведение миграций

#работаем с models.py для создания табличек

#создание миграций
#python manage.py makemigrations
#Migrations for 'blog':
#   blog\migrations\0001_initial.py
#     - Create model News

# python manage.py sqlmigrate blog 0001 - просмотр SQL-команд,которые будут выполнятся
# BEGIN;
# --
# -- Create model News
# --
# CREATE TABLE "blog_news" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100)
#  NOT NULL, "text" text NOT NULL, "date" datetime NOT NULL, "avtor_id" integer NOT NULL REFERENCES "auth_user"
#  ("id") DEFERRABLE INITIALLY DEFERRED);
# CREATE INDEX "blog_news_avtor_id_27c6f81f" ON "blog_news" ("avtor_id");
# COMMIT;

# python manage.py migrate - проведение миграций
#миграцию нужно регистрировать в admin.py:
#from .models import News
#admin.site.register(News)

#после правок надо опять проводить миграции
#python manage.py makemigrations
# Migrations for 'blog':
#   blog\migrations\0002_alter_news_options_alter_news_avtor_alter_news_date.py
#     - Change Meta options on news
#     - Alter field avtor on news
#     - Alter field date on news

# python manage.py migrate 

#получаем все данные из таблички на сайте в папку views.py
#from .models import News
#теперь подставляем 'news': News.objects.all()
#QuerySet - список состоящий из обьектов,где ключи это title data и т.д.

#Django date - форматы даты в Джанго
#https://docs.djangoproject.com/en/5.0/ref/templates/builtins/
#{{ post.date|date:"j F Y, время: H:i:s" }}<
