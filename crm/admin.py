from django.contrib import admin
from crm import models
from rest_framework_api_key.models import  APIKey
# Register your models here.
admin.register(models.UserProfile)
