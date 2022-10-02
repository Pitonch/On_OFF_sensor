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
def sensor(request, status: str):
    url_sensor1 = 'http://192.168.0.89/'
    switch = requests.get(url_sensor1 + f'cm?cmnd=Power%20{status}')
    print(switch)
    switch.raise_for_status()
    result = switch.json()
    print(result)
    return JsonResponse(result)
