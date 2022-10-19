import requests
from django.shortcuts import render, redirect
from .models import Sensor, Location
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import urllib3


def home(request):
    # print(request.user)
    return render(request, 'interaction/base.html')


def about(request):
    return render(request, 'interaction/about.html', {'content': '<h1>About</h1>'})


def settings(request):
    return render(request, 'interaction/settings.html', {'content': '<h1>Settings On_OFF_sensor</h1>'})


def commands(request):
    return render(request, 'interaction/commands.html', {'content': '<h1>Commands</h1>'})


def next_pages(request):
    return render(request, 'interaction/next.html', {'content': '<h1>next</h1>'})


# вывод всех датчиков


def show_sensors(request):
    all_ip_sensors = Sensor.objects.all()
    # print(all_ip_sensors)
    return render(request, "interaction/all_sensors.html", {'all_ip_sensors': all_ip_sensors})


def ip_(request, ip_sensor):
    data = {'ip_sensor': ip_sensor}
    return render(request, "interaction/commands.html", context=data)


# def sensor_(request, ip_sensor, status):
#     sensor = Sensor.objects.get(ip_sensor=ip_sensor)
#     sensor.status = status
#     print('status:', sensor_)
#     return render(request, "interaction/commands_status.html", {'status': status})


def sensor_on_off(request, ip_sensor, status_sensor):
    print('START')
    print(ip_sensor)
    switch = requests.post('http://' + ip_sensor + f'/cm?cmnd=Power%20{status_sensor}')
    print(switch)
    print('status:', status_sensor)
    sensor = Sensor.objects.get(ip_sensor=ip_sensor)
    sensor.status_sensor = status_sensor
    sensor.save(update_fields=["status_sensor"])
    switch.raise_for_status()
    result = switch.json()
    print('result:', result)
    return redirect('/interaction/commands/' + ip_sensor, JsonResponse(result))
    # доработать через ajax
    # return JsonResponse(result)


# получение данных из бд
def index(request):
    # фильтрация
    guest = User.objects.all()
    return render(request, "interaction/index.html", {"guest": guest})


# добавление данных в бд
def create(request):
    initialize()
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        guest = User()
        guest.name = request.POST.get("name")
        location_ids = request.POST.getlist("location")
        guest.save()
        # получаем все выбранные курсы по их id
        location = Location.objects.filter(id__in=location_ids)
        guest.location.set(location, through_defaults={"mark": 0})
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    location = Location.objects.all()
    return render(request, "interaction/create.html", {"location": location})


def initialize():
    # Student.objects.all().delete()
    # Course.objects.all().delete()
    if Location.objects.all().count() == 0:
        Location.objects.create(name="room1")
        Location.objects.create(name="room2")
        Location.objects.create(name="room3")


def show_guest(request):
    all_guest = User.objects.all()
    print(all_guest)
    return render(request, "interaction/showguest.html", {'all_guest': all_guest})


# функция вывода постов для определенного гостя

@login_required
def show_guest_location(request):
    # создается список из имен доступных для пользователя зон
    available_locations = []
    for location in Location.objects.filter(guest=request.user):
        available_locations.append(location.name_location)

    # Фильтруем датчики так, чтобы выбрать только те, которые находятся в этих зонах

    available_sensor = Sensor.objects.filter(location__name_location__in=available_locations)
    return render(request, "interaction/show_guest_location.html", {'available_sensor': available_sensor})


#опрос датчика
def sensor_ping(request):
    http = urllib3.PoolManager()
    url_sensor = 'http://192.168.0.89/cm?cmnd=Status0'
    response = http.request('GET', url_sensor)
    print(response.status)
    return response.status
