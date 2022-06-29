from django.utils import timezone, dateformat
from django_seed import Seed
from django_seed.seeder import ModelSeeder
from django_seed.providers import Provider
from crm.models import Environment, AirConditioning, Lamp, EnvironmentState
import random

seeder = Seed.seeder()

seeder.add_entity(Environment, 3, {
    'name': lambda x: seeder.faker.name(),
    'local': lambda x: seeder.faker.street_address(),
    't_t': lambda x: random.randrange(20, 30, 1),
    't_a': lambda x: random.randrange(20, 30, 1),
    'umd': lambda x: random.randrange(30, 90, 1),
    'n_g': lambda x: random.randrange(0, 600, 100),
    'created_at': lambda x: timezone.now(),
    'updated_at': lambda x: timezone.now()
})

seeder.add_entity(AirConditioning, 10, {
    'environment': lambda x: Environment.objects.get(id=(random.randint(1, Environment.objects.count()))),
    'power': lambda x: random.randrange(900, 1500, 100),
    'brand': lambda x: seeder.faker.name(),
    'model': lambda x: seeder.faker.name(),
    'on_off': lambda x: random.randint(0, 1),
})

seeder.add_entity(Lamp, 20, {
    'environment': lambda x: Environment.objects.get(id=(random.randint(1, Environment.objects.count()))),
    'power': lambda x: random.randrange(15, 35, 1),
    'brand': lambda x: seeder.faker.name(),
    'model': lambda x: seeder.faker.name(),
    'on_off': lambda x: random.randint(0,1),
})


seeder.add_entity(EnvironmentState, 1000, {
    'environment': lambda x: Environment.objects.get(id=(random.randint(1, Environment.objects.count()))),
    't_a': lambda x: random.randrange(20, 30, 1),
    'umd': lambda x: random.randrange(30, 90, 1),
    'n_g': lambda x: random.randrange(0, 600, 100),
    'created_at': lambda x: timezone.now()
})

seeder.execute()
