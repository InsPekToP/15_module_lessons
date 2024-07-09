from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField('Название статьи',max_length=100)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField(default=timezone.now)
    avtor = models.ForeingKey(User, on_delete=models.CASCADE)
