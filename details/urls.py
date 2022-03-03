from django.contrib import admin
from django.urls import path

from . import views

app_name = 'stud'
urlpatterns = [
    path('', views.index, name="index"),
    path('result/', views.result, name='result')
]
