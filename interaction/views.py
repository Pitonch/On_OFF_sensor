import requests
from django.shortcuts import render, redirect
from .models import Sensor, Location
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User


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
    #доработать через ajax
    # return JsonResponse(result)


# получение данных из бд
def index(request):
    # фильтрация
    user = User.objects.all()
    return render(request, "interaction/index.html", {"user": user})


# добавление данных в бд
def create(request):
    initialize()
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        user = User()
        user.name = request.POST.get("name")
        location_ids = request.POST.getlist("location")
        user.save()
        # получаем все выбранные курсы по их id
        location = Location.objects.filter(id__in=location_ids)
        user.location_set.set(location, through_defaults={"mark": 0})
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    location = Location.objects.all()
    return render(request, "interaction/create.html", {"location": location})


def initialize():
    # Student.objects.all().delete()
    # Course.objects.all().delete()
    if Location.objects.all().count() == 0:
        Location.objects.create(name="room1")





























#записm IP и room in On_OFF_sensor_db
# получение данных из бд


# def index(request):
#     #много сенсоров
#     sensors = OnOffSensor.objects.all()
#     return render(request, "interaction/settings.html", {"sensors": sensors})
#
#
# # сохранение данных в бд создание 1 сенсора
# def create(request):
#     if request.method == "POST":
#         sensor = OnOffSensor()
#         sensor.ip = request.POST.get("ip")
#         sensor.room = request.POST.get("room")
#         sensor.save()
#     return HttpResponseRedirect("/")
#
#
# # изменение данных в бд
# def edit(request, sensor_id):
#     try:
#         sensor = OnOffSensor.objects.get(id=sensor_id)
#
#         if request.method == "POST":
#             sensor.ip = request.POST.get("ip")
#             sensor.room = request.POST.get("room")
#             sensor.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "interaction/edit_settings.html", {"sensor": sensor})
#     except OnOffSensor.DoesNotExist:
#         return HttpResponseNotFound("<h2>Sensor not found</h2>")
#
#
# # удаление данных из бд
# def delete(request, sensor_id):
#     try:
#         sensor = OnOffSensor.objects.get(id=sensor_id)
#         sensor.delete()
#         return HttpResponseRedirect("/")
#     except OnOffSensor.DoesNotExist:
#         return HttpResponseNotFound("<h2>Sensor not found</h2>")
#
#





