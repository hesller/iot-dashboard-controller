from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from crm import views
from crm import decorators as dc

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('painel/', views.dashboard, name='dashboard'),
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("cadastrar/", login_required(views.RegisterView.as_view()), name='register'),
    path("ambientes/", login_required(views.EnvironmentListView.as_view()), name='list-environments'),
    path("ambientes/criar", login_required(views.EnvironmentCreateView.as_view()), name='create-environments'),
]