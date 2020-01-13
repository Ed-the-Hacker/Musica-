from django.urls import path
from . import views

urlpatterns = [
    path('', views.canciones_list, name='canciones_list'),
]