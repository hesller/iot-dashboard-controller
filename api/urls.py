from django.urls import path
from api import views

urlpatterns = [
    path('environments/', views.EnvironmentsList.as_view(), name='environments-list')
]