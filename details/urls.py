from django.contrib import admin
from django.urls import path

from . import views

app_name = 'stud'
urlpatterns = [
    path('', views.index, name="index"),
    path('result/', views.result, name='result'),
    path('result/<int:pk>/edit/', views.editstudent, name='edit'),
    path('result/<int:pk>/delete/', views.deletestudent, name='delete')
]
