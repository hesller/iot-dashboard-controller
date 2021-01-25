from rest_framework import serializers
from crm import models as crm_models


class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = crm_models.Environment
        fields=['']
