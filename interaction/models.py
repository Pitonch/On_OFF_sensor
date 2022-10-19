from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    name_home = models.CharField(max_length=100)
    descriptions_home = models.CharField(max_length=100)

    def __str__(self):
        return self.name_home


class Location(models.Model):
    name_location = models.CharField(max_length=100)
    descriptions_location = models.CharField(max_length=100)
    home = models.ForeignKey(Home, on_delete=models.SET_NULL, null=True, related_name='home')
    guest = models.ManyToManyField(User, null=True, blank=True)  # Чтобы можно было не указывать пользователя

    def __str__(self):
        return f'{self.name_location} ({self.home.name_home})'  # Чтобы отображался еще и Home


class Sensor(models.Model):
    ip_sensor = models.GenericIPAddressField(unique=True, protocol='IPv4')
    name_sensor = models.CharField(max_length=100)
    descriptions_sensor = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='location')
    status_sensor = models.CharField(max_length=5)

    # def __str__(self):
    #     return self.name_sensor




