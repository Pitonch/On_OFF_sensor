from django.db import models


class OnOffSensor(models.Model):
    ip = models.GenericIPAddressField()
    room = models.CharField(max_length=50)



