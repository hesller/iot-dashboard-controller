# Generated by Django 3.1.5 on 2021-01-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20210126_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='lamp',
            name='brand',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lamp',
            name='model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]