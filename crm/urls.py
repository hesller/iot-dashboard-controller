from django.contrib import admin
from django.urls import path
from crm import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("cadastrar/", views.RegisterView.as_view(), name='register'),
    path("ambientes/", views.EnvironmentListView.as_view(), name='list-environments'),
    path("ambientes/criar", views.EnvironmentCreateView.as_view(), name='create-environments'),
]