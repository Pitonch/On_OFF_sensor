from On_OFF_sensor.celery import app
from django.shortcuts import get_object_or_404
from ping3 import ping
import requests
from .models import Sensor
from django.http import JsonResponse


@app.task
def ping_sensor():
    # Проверка доступности датчика
    for sensor in Sensor.objects.all(): #для всех датчиков в Sensor
        if ping(sensor.ip_sensor): #если датчик пинг
            sensor = Sensor.objects.get(ip_sensor=sensor.ip_sensor) #находим датчик по ip
            # sensor.status_sensor = sensor.status_sensor #получаем его статус
            sensor.save(update_fields=["status_sensor"]) #записываем стату в базу данных
            print(sensor.ip_sensor, '1:', sensor.status_sensor)

        else: # Датчик не доступен по пингу
            sensor = Sensor.objects.get(ip_sensor=sensor.ip_sensor) #находим датчик по ip
            sensor.status_sensor = 'down' #присваиваем статус 'down'
            sensor.save(update_fields=["status_sensor"]) #записываем стату в базу данных
            print(sensor.ip_sensor, '2:', sensor.status_sensor)

        print(sensor.ip_sensor, '3:', sensor.status_sensor)






#
# @app.task
# def ping_sensor():
#     ip_sensor = '192.168.0.89'
#     if ping(ip_sensor, timeout=1):
#         return 'sensor online ping'
#     else:
#         return 'sensor offline ping'
#
# print(ping_sensor())
