from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from crm import models as crm_models

from api import serializers as api_serializer


class EnvironmentsList(ListAPIView):
    queryset = crm_models.Environment.objects.all()
    serializer_class = api_serializer.EnvironmentSerializer
    permission_classes = [IsAuthenticated]
