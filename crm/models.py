from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.db.models import Deferrable, UniqueConstraint

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,name,email,password=None):
        """This function creates a new user"""
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using='default')

        return user

    def create_superuser(self, name, email, password):
        """Creates a new superuser with the details"""
        user = self.create_user(name=name,email=email,password=password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using='default')


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the user in the system"""
    name = models.CharField(max_length=255, )
    email = models.EmailField(max_length=255, unique=True)
    profile_picture = models.ImageField(blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_fullname(self):
        """Retrieve fullname of the user"""
        return self.name

    def get_shortname(self):
        """Retrieve short name"""
        return self.name

    def __str__(self):
        """Return string representation of the user"""
        return f"{self.id} - {self.name} - {self.email}"


class Environment(models.Model):
    name = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    t_a = models.FloatField(blank=True, null=True)
    t_t = models.FloatField(blank=True, null=True)
    umd = models.FloatField(blank=True, null=True)
    n_g = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False, auto_now=True)
    updated_at = models.DateTimeField(editable=True, auto_now_add=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Environment, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} | {self.name} | {self.local} | {self.t_a if self.t_a else 0.0} | {self.t_t if self.t_t else 0.0}" \
               f" | {self.umd if self.umd else 0} | {self.n_g if self.n_g else 0}"


class EnvironmentState(models.Model):
    environment = models.ForeignKey(Environment, related_name='sensor_data', on_delete=models.CASCADE)
    t_a = models.FloatField(blank=True, default=0.0)
    umd = models.FloatField(blank=True, default=0.0)
    n_g = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        ordering = ['created_at']
        constraints = [
            UniqueConstraint(fields=['environment', 'created_at'], name='unique_room_data')
        ]

    def __str__(self):
        return f"{self.t_a},{self.umd},{self.n_g},{self.created_at}"


class AirConditioning(models.Model):
    environment = models.ForeignKey(Environment, related_name='acs', on_delete=models.CASCADE)
    power = models.FloatField(default=0)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    on_off = models.BooleanField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.id} | Ar-condicionado {self.brand}, {self.model} | {self.environment.name} | Status: {'ligado' if self.on_off else 'desligado'}"


class Lamp(models.Model):
    environment = models.ForeignKey(Environment, related_name='lamps', on_delete=models.CASCADE)
    power = models.FloatField(default=0)
    brand = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    on_off = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.id} | Lampada {self.power} watts | {self.environment.name} | Status: {'ligado' if self.on_off else 'desligado'}"