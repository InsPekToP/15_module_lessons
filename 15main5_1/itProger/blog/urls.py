from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('contacti/some/123',views.contacti),
]