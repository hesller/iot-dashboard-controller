# Generated by Django 3.1.6 on 2021-02-05 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
                ('t_a', models.FloatField(blank=True, null=True)),
                ('t_t', models.FloatField(blank=True, null=True)),
                ('umd', models.FloatField(blank=True, null=True)),
                ('n_g', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.FloatField(default=0)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('on_off', models.BooleanField(default=0)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lamps', to='crm.environment')),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_a', models.FloatField(blank=True, default=0.0)),
                ('umd', models.FloatField(blank=True, default=0.0)),
                ('n_g', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_data', to='crm.environment')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='AirConditioning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.FloatField(default=0)),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('on_off', models.BooleanField(default=0)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acs', to='crm.environment')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='environmentstate',
            constraint=models.UniqueConstraint(fields=('environment', 'created_at'), name='unique_room_data'),
        ),
    ]
