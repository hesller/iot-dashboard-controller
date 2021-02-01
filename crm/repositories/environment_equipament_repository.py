from crm import models


def get_all_equipament_environment(context, curr_obj):
    acs = models.AirConditioning.objects.filter(environment=curr_obj)
    lamps = models.Lamp.objects.filter(environment=curr_obj)
    context['acs'] = acs
    context['lamps'] = lamps
    context['env_id'] = curr_obj.id
    return context

