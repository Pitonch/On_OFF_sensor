import urllib3
import json
# from ping3 import ping
import requests
# from django.shortcuts import render, redirect
# from .models import Sensor
# from django.http import JsonResponse, HttpResponseRedirect
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404
# from .tasks import ping_sensor



http = urllib3.PoolManager()
url = 'http://192.168.0.89/cm?cmnd=Status'
resp = http.request('GET', url)
# print(resp.status)
if resp.status == 200:
    print('sensor online')
    print(resp.data.decode('utf-8'))


# def ping_sensor():
#     ip_sensor = '192.168.0.89'
#     if ping(ip_sensor, timeout=1):
#         return 'sensor online ping'
#     else:
#         return 'sensor offline ping'
#
# print(ping_sensor())

# def ping_sensor(request, ip_sensor, status_sensor):
#     # Проверка доступности датчика
#     sensor = get_object_or_404(Sensor, ip_sensor=ip_sensor)
#     sensor.status_sensor = status_sensor
#     sensor.save(update_fields=["status_sensor"])
#     return 'sensor online ping'
#
#     # else:
#     #     # Датчик надоступен по пингу записываем его статус в базу данных
#     #     sensor = Sensor.objects.get(ip_sensor=ip_sensor)
#     #     sensor.status_sensor = 'down'
#     #     sensor.save(update_fields=["status_sensor"])
#     #     return 'sensor offline ping'


# print(ping_sensor())
#
# def sensor_get_information():
#     http = urllib3.PoolManager()
#     url_sensor = 'http://192.168.0.89/cm?cmnd=Status1'
#     response = http.request('GET', url_sensor)
#     return response
#
#
# print(sensor_get_information())


# http = urllib3.PoolManager()
# r = http.request(
#     'POST',
#     'http://192.168.0.89/cm?cmnd=Status1',
#     )
# print(r.status)
# print('type_r:', type(r))
# sensor_dict = json.loads(r.data)
# print('type_r:', type(sensor_dict))
# print(sensor_dict)
# print('status:', sensor_dict["Status"]["Power"])
#
# print(json.loads(r.data.decode('utf-8')))

r = requests.get("http://192.168.0.89/cm?cmnd=Status0")
sensor_dict = r.json()
for key in sensor_dict["Status"]:
    print(key)
for value in sensor_dict["Status"]:
    print(value)

# print(sensor_dict["Status"]["Power"])
# a=sensor_dict["StatusSTS"]["POWER"]
# print(sensor_dict)
# print(type(sensor_dict["Status"]))
# for key in sensor_dict["Status"]:
#     print(key)

# def info_sensor(request):
#     for sensor in Sensor.objects.all(): #для всех датчиков в Sensor
#         sensor = Sensor.objects.get(ip_sensor=sensor.ip_sensor) #находим датчик по ip
#         if ping(sensor.ip_sensor, timeout=1): #если датчик пинг таймер 1 cек
#             url = f'http://{sensor.ip_sensor}/cm?cmnd=Status'
#             response = requests.get(url) #получаем ответ
#             print(response)
#             sensor_dict = response.json() #переводим его в словарь
#             for key_sensor in sensor_dict["Status"]:
#                 print(key_sensor)
#                 return render(request, "interaction/commands.html", {'key_sensor': key_sensor})
#             for value_sensor in sensor_dict["Status"]:
#                 return render(request, "interaction/commands.html", {'value_sensor': value_sensor})








# @app.task
# def ping_sensor():
#     # Проверка доступности датчика
#     for sensor in Sensor.objects.all(): #для всех датчиков в Sensor
#         if ping(sensor.ip_sensor, timeout=1): #если датчик пинг таймер 1 cек
#             http = urllib3.PoolManager()
#             url = f'http://{sensor.ip_sensor}/cm?cmnd=Status1'
#             # print(("sensor.ip_sensor", sensor.ip_sensor))
#             # url = 'http://192.168.0.89/cm?cmnd=Status1'
#             response = http.request(
#                 'POST',
#                 url)
#             if response.status == 200:
#                 sensor_dict = json.loads(response.data) #то ответ переводим в словарь в виде json
#                 status_and_power = sensor_dict["Status"]["Power"]
#                 sensor = Sensor.objects.get(ip_sensor=sensor.ip_sensor) #находим датчик по ip
#                 sensor.status_sensor = status_and_power #получаем его статус
#                 sensor.save(update_fields=["status_sensor"]) #записываем статус в базу данных
#                 print(('ip sensor + sensor status: 1', sensor.ip_sensor, sensor.status_sensor))
#             else:
#                 sensor = Sensor.objects.get(ip_sensor=sensor.ip_sensor)  # находим датчик по ip
#                 sensor.status_sensor = 'down'  # присваиваем статус 'down'
#                 sensor.save(update_fields=["status_sensor"])  # записываем стату в базу данных
#                 print(('ip sensor + sensor status: 2', sensor.ip_sensor, sensor.status_sensor))
#
#
#         else: # Датчик не доступен по пингу
#             sensor = Sensor.objects.get(ip_sensor=sensor.ip_sensor) #находим датчик по ip
#             sensor.status_sensor = 'down' #присваиваем статус 'down'
#             sensor.save(update_fields=["status_sensor"]) #записываем стату в базу данных
#             print(('ip sensor + sensor status: 3', sensor.ip_sensor, sensor.status_sensor))






