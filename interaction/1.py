from ping3 import ping
import requests
from django.shortcuts import render, redirect
from .models import Sensor
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .tasks import ping_sensor



# http = urllib3.PoolManager()
# url = 'http://192.168.0.89/cm?cmnd=Status'
# resp = http.request('GET', url)
# # print(resp.status)
# try:
#     if resp.status == 200:
#         print('sensor online')
#         print(resp.data.decode('utf-8'))
# except TimeoutError:
#     print('sensor offline')

# def ping_sensor():
#     ip_sensor = '192.168.0.89'
#     if ping(ip_sensor, timeout=1):
#         return 'sensor online ping'
#     else:
#         return 'sensor offline ping'
#
# print(ping_sensor())


def ping_sensor(ip_sensor, status_sensor):
    # Проверка доступности датчика
    if ping(ip_sensor):
        sensor = get_object_or_404(Sensor, ip_sensor=ip_sensor)
        sensor.status_sensor = status_sensor
        sensor.save(update_fields=["status_sensor"])
        return True

    else:
        # Датчик надоступен по пингу записываем его статус в базу данных
        sensor = Sensor.objects.get(ip_sensor=ip_sensor)
        sensor.status_sensor = 'down'
        sensor.save(update_fields=["status_sensor"])
        return False





