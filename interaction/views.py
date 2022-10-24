from ping3 import ping
import requests
from django.shortcuts import redirect
from .models import Sensor, Location, Image
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# import urllib3
from django.shortcuts import render


def home(request):
    # print(request.user)
    return render(request, 'interaction/base.html')


def about(request):
    data = Image.objects.all()
    return render(request, 'interaction/about.html', {'data': data})

# вывод всех датчиков


@login_required
def show_sensors(request):
    # создается список из имен доступных для пользователя зон
    if request.user.is_superuser:
        # Для суперпользователя видно все
        all_ip_sensors = Sensor.objects.all()
    else:
        available_locations = []
        for location in Location.objects.filter(guest=request.user):
            available_locations.append(location.name_location)
        # Фильтруем датчики так, чтобы выбрать только те, которые находятся в этих зонах
        all_ip_sensors = Sensor.objects.filter(location__name_location__in=available_locations)
    return render(request, "interaction/all_sensors.html", {'all_ip_sensors': all_ip_sensors})

# вывод ip датчика


def ip_(request, ip_sensor):
    if ping(ip_sensor, timeout=1):  # если датчик пинг таймер 1 cек
        url = f'http://{ip_sensor}/cm?cmnd=Status'
        print('url:', url)
        response = requests.get(url)  # получаем ответ
        print(response)
        sensor_dict = response.json()  # переводим его в словарь
        print('sensor_dict type:', type(sensor_dict))
        print('sensor_dict:', sensor_dict)
        data = {'ip_sensor': ip_sensor, 'sensor_dict': sensor_dict}
        return render(request, "interaction/commands.html", context=data)
    else:
        sensor = Sensor.objects.get(ip_sensor=ip_sensor)
        print('status_sensor:', sensor.status_sensor)
        data = {'ip_sensor': ip_sensor, 'status_sensor': sensor.status_sensor}
        return render(request, "interaction/commands.html", context=data)


# функция управления сенсорами

def sensor_on_off(request, ip_sensor, status_sensor):
    # Проверка доступности датчика
    if ping(ip_sensor):  # Если датчик пингуется
        # Если нет датчика, то вернется код 404
        sensor = get_object_or_404(Sensor, ip_sensor=ip_sensor)
        sensor.status_sensor = status_sensor
        sensor.save(update_fields=["status_sensor"])  # Обновляем поле в базе данных
        # Отправляем запрос на датчик
        switch = requests.post('http://' + ip_sensor + f'/cm?cmnd=Power%20{status_sensor}')
        switch.raise_for_status()
        result = switch.json()  # получаем словарь после запроса
        return redirect('/interaction/allsensors/', JsonResponse(result))
    else:
        # Датчик не доступен по ping записываем его статус в базу данных
        sensor = Sensor.objects.get(ip_sensor=ip_sensor)
        sensor.status_sensor = 'down'  # Обновляем поле в базе данных данным по умолчанию
        sensor.save(update_fields=["status_sensor"])
        return redirect('/interaction/allsensors/', JsonResponse({'status': 'down'}))
