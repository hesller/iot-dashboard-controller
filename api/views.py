from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework_api_key.permissions import HasAPIKey

from crm import models as crm_models

from api import serializers as api_serializer


class EnvironmentsList(ListAPIView):
    queryset = crm_models.Environment.objects.all()
    serializer_class = api_serializer.EnvironmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EnvironmentCreate(CreateAPIView):
    queryset = crm_models.Environment.objects.all()
    serializer_class = api_serializer.EnvironmentCreateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        print(response.data)
        return redirect('environments-list')


class AirContinioning(ListAPIView):
    queryset = crm_models.AirConditioning.objects.all()
    serializer_class = api_serializer.AirConditioningSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class Dht11Sensor(UpdateAPIView):
    serializer_class = api_serializer.SensorDht11Serializer
    queryset = crm_models.Environment.objects.all()


class EnvironmentUpdateState(CreateAPIView):
    queryset = crm_models.EnvironmentState.objects.all()
    serializer_class = api_serializer.EnvironmentStateSerializer
    permission_classes = [IsAuthenticated]


class EnvironmentStateList(ListAPIView):
    queryset = crm_models.Environment.objects.all()
    serializer_class = api_serializer.EnvironmentStateListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    



