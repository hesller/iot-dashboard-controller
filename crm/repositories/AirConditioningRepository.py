from crm import models


def getAcWithEnvID(pk=1):
    ac = models.AirConditioning.objects.get(pk)
    env_id = ac.environment.id
    return ac, env_id