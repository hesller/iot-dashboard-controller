from rest_framework import serializers
from crm import models as crm_models


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = crm_models.Environment
        fields = "__all__"


class EnvironmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = crm_models.Environment
        fields = ['name', 'local', 't_t']


class AirConditioningSerializer(serializers.ModelSerializer):
    class Meta:
        model = crm_models.AirConditioning
        fields = "__all__"
