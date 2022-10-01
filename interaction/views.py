import requests
from django.shortcuts import render
from django.http import JsonResponse



def home(request):
    # print(request.user)
    return render(request, 'interaction/base.html')


def about(request):
    return render(request, 'interaction/about.html', {'content': '<h1>About</h1>'})


def settings(request):
    return render(request, 'interaction/settings.html', {'content': '<h1>Settings On_OFF_sensor</h1>'})


def commands(request):
    return render(request, 'interaction/commands.html', {'content': '<h1>Сommands</h1>'})


def next_pages(request):
    return render(request, 'interaction/next.html', {'content': '<h1>next</h1>'})


# отправляем запрос GET на датчик (IP получаем через регистрации по WIFI).
def on_sensor(res_on):
    url_sensor1 = 'http://192.168.0.89/'
    on = 'cm?cmnd=Power%20On'
    res_on = requests.get(url_sensor1+on)
    print(res_on)
    res_on.raise_for_status()
    JsonResponse = res_on.json()
    print(JsonResponse)
    return JsonResponse


def off_sensor(res_off):
    url_sensor1 = 'http://192.168.0.89/'
    off = 'cm?cmnd=Power%20off'
    res_off = requests.get(url_sensor1 + off)
    # res_off.raise_for_status()
    jsonResponse = res_off.json()
    print(jsonResponse)
    return jsonResponse







