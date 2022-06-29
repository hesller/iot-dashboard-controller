from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from crm import views
from crm import decorators as dc

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('painel/', login_required(views.DashboardView.as_view()), name='dashboard'),
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.LogoutView.as_view(), name='logout'),
    path("cadastrar/", login_required(views.RegisterView.as_view()), name='register'),
    path("ambientes/", login_required(views.EnvironmentListView.as_view()), name='list-environments'),
    path("ambientes/criar", login_required(views.EnvironmentCreateView.as_view()), name='create-environments'),
    path("ambientes/criar/novo/", login_required(views.EnvironmentCreateView.as_view()), name='create-new-environment'),
    path("ambientes/editar/<int:pk>/", login_required(views.EnvironmentDetails.as_view()), name='edit-environment'),
    path("ambientes/deletar/<int:pk>/", login_required(views.EnvironmentDelete.as_view()), name='delete-environment'),
    path("ambientes/editar/<int:env>/arcondicionado/<int:pk>/", login_required(views.AirConditionUpdate.as_view()),
         name='update-ac-environment'),
    path("ambientes/<int:env_id>/ar-condicionado/criar/", login_required(views.AirconditioningCreate.as_view()),
         name='create-ac'),
    path("ambientes/ar-condicionado/<int:pk>/", login_required(views.AirConditionUpdate.as_view()),
         name='update-ac-of-environment'),
    path("ambientes/<int:env_id>/lampadas/criar/", login_required(views.LampCreate.as_view()), name='create-lamp'),

    path("ambientes/<int:env>/deletar/ar-condicionado/<int:pk>/", login_required(views.AirConditioningDelete.as_view()),
         name='delete-ac-environment'),
    path("ambientes/editar/<int:env>/lampadas/<int:pk>/", login_required(views.LampUpdate.as_view()),
         name='update-lamp-environment'),
    path("ambientes/<int:env>/deletar/lampada/<int:pk>/", login_required(views.LampDelete.as_view()),
         name='delete-lamp-environment'),
]
