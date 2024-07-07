from django.urls import path
#из этой же директории импорт views.py(в той же папке находится)
from . import views

urlpatterns = [
    path('',views.home),
    path('contacti',views.contacti)
]