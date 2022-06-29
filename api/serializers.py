from django.utils import timezone
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


class SensorDht11Serializer(serializers.Serializer):
    t_a = serializers.FloatField()
    umd = serializers.FloatField()
    updated_at = serializers.DateTimeField(default=timezone.now(), format="%d-%m-%Y %H:%M:%S")


class EnvironmentStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = crm_models.EnvironmentState
        fields = '__all__'


class EnvironmentStateListSerializer(serializers.ModelSerializer):
    sensor_data = serializers.SerializerMethodField()
    curr_temp = serializers.SerializerMethodField()

    class Meta:
        model = crm_models.Environment
        fields = ['id','name', 'local', 't_t', 'sensor_data', 'curr_temp']

    def get_sensor_data(self, environment):
        qs = crm_models.EnvironmentState.objects.filter(environment=environment.id).order_by('-created_at')[:100]
        return EnvironmentStateSerializer(qs, many=True, read_only=True).data

    def get_curr_temp(self, environment):
        qs = crm_models.EnvironmentState.objects.filter(environment=environment.id).order_by('id').last()
        return EnvironmentStateSerializer(qs, read_only=True).data

