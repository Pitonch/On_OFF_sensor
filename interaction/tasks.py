from On_OFF_sensor.celery import app
from django.shortcuts import get_object_or_404
from ping3 import ping
import requests
from .models import Sensor
from django.http import JsonResponse


@app.task
def ping_sensor(ip_sensor, status_sensor):
    # Проверка доступности датчика
    if ping(ip_sensor):
        for sensor in Sensor.objects.all():
            # sensor = get_object_or_404(Sensor, ip_sensor=ip_sensor)
            sensor.status_sensor = status_sensor
            sensor.save(update_fields=["status_sensor"])
            return ip_sensor


    else:
        # Датчик надоступен по пингу записываем его статус в базу данных
        sensor = Sensor.objects.get(ip_sensor=ip_sensor)
        sensor.status_sensor = 'down'
        sensor.save(update_fields=["status_sensor"])






# @app.task
# def ping_sensor():
#     ip_sensor = '192.168.0.89'
#     if ping(ip_sensor, timeout=1):
#         return 'sensor online ping'
#     else:
#         return 'sensor offline ping'
#
# print(ping_sensor())
