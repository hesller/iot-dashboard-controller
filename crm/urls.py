from django.contrib import admin
from django.urls import path
from crm import views

urlpatterns = [
    path('', views.home),
]