from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


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
        user.save(using='default')


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for the user in the system"""
    name = models.CharField(max_length=255, )
    email = models.EmailField(max_length=255, unique=True)
    profile_picture = models.ImageField(blank=True)
    is_active = models.BooleanField(default=False)

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
    t_a = models.FloatField(blank=True)
    t_t = models.FloatField(blank=True)
    umd = models.FloatField(blank=True)
    n_g = models.FloatField(blank=True)

    def __str__(self):
        return f"{self.id} | {self.name} | {self.local} | {self.t_a if self.t_a else 0.0} | {self.t_t if self.t_t else 0.0}" \
               f" | {self.umd if self.umd else 0} | {self.n_g if self.n_g else 0}"


class AirConditioning(models.Model):
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    power = models.FloatField(default=0)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    on_off = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.id} | Ar-condicionado {self.brand}, {self.model} | Status: {'ligado' if self.on_off else 'desligado'}"


class Lamp(models.Model):
    environment = models.ForeignKey(Environment,  on_delete=models.CASCADE)
    power = models.FloatField(default=0)
    on_off = models.BooleanField(default=0)

    def __str__(self):
        return f"{self.id} | Lampada {self.power} watts | Status: {'ligado' if self.on_off else 'desligado'}"