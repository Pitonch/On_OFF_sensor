from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=100)
    home = models.ForeignKey(Home, on_delete=models.SET_NULL, null=True, related_name='home')


class Sensor(models.Model):
    ip = models.GenericIPAddressField()
    name = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=100)
    location = models.ForeignKey(Home, on_delete=models.SET_NULL, null=True, related_name='location')




