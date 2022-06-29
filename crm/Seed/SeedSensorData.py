from django.utils import timezone, dateformat
from django_seed import Seed
from django_seed.seeder import ModelSeeder
from django_seed.providers import Provider
from crm.models import Environment, AirConditioning, Lamp, EnvironmentState
import random

seeder = Seed.seeder()

seeder.add_entity(EnvironmentState, 1000, {
    'environment': lambda x: Environment.objects.get(id=(random.randint(1, Environment.objects.count()))),
    't_a': lambda x: random.randrange(20, 30, 1),
    'umd': lambda x: random.randrange(30, 90, 1),
    'n_g': lambda x: random.randrange(0, 600, 100),
    'created_at': lambda x: timezone.now()
})

seeder.execute()
