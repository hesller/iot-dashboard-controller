# Generated by Django 3.1.5 on 2021-01-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_airconditioning_environment_lamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
