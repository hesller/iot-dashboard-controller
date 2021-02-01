from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, ListCreateAPIView
from django.shortcuts import redirect

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


