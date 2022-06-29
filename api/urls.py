from django.urls import path
from api import views

urlpatterns = [
    path('environments/', views.EnvironmentsList.as_view(), name='environments-list'),
    path('environments/create/', views.EnvironmentCreate.as_view(), name='environments-create'),
    path('air_conditioning/', views.AirContinioning.as_view(), name='air-conditioning-list'),
    path('environments/update/<int:pk>/', views.Dht11Sensor.as_view(), name='update-dht11'),
    path('environments/state/', views.EnvironmentStateList .as_view(), name='environment-state'),
]