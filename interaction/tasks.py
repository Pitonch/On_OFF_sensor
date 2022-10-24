from On_OFF_sensor.celery import app
from ping3 import ping
import requests
from .models import Sensor


@app.task
def ping_sensor():  # Проверка доступности датчика

    for sensor in Sensor.objects.all():  # для всех датчиков в Sensor
        sensor = Sensor.objects.get(ip_sensor=sensor.ip_sensor)  # находим датчик по ip
        if ping(sensor.ip_sensor, timeout=1):  # если датчик пинг таймер 1 cек
            url = f'http://{sensor.ip_sensor}/cm?cmnd=Status0'  # отправляем запрос
            response = requests.get(url)  # получаем ответ
            sensor_dict = response.json()  # переводим его в словарь
            sensor.status_sensor = sensor_dict["StatusSTS"]["POWER"]  # получаем его статус
            print(('ip sensor + sensor status: ping', sensor.ip_sensor, sensor.status_sensor))
        else:  # Датчик не доступен по ping
            sensor.status_sensor = 'down'  # присваиваем статус 'down'
            print(('ip sensor + sensor status: no ping', sensor.ip_sensor, sensor.status_sensor))
        sensor.save(update_fields=["status_sensor"])  # записываем статуc в базу данных
