from django.db import models


class Home(models.Model):
    name_home = models.CharField(max_length=100)
    descriptions_home = models.CharField(max_length=100)

    def __str__(self):
        return self.name_home


class Location(models.Model):
    name_location = models.CharField(max_length=100)
    descriptions_location = models.CharField(max_length=100)
    home = models.ForeignKey(Home, on_delete=models.SET_NULL, null=True, related_name='home')

    def __str__(self):
        return self.name_location


class Sensor(models.Model):
    ip_sensor = models.GenericIPAddressField()
    name_sensor = models.CharField(max_length=100)
    descriptions_sensor = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='location')

    def __str__(self):
        return self.name_sensor




