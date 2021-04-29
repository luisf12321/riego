import json

from django.http import HttpResponse
from datetime import datetime


def hello_world(request):
    now1 = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('hello, world. time is {now}'.format(now=now1))


def hi(request):
    print(request.GET['numbers'])
    numbers = request.GET['numbers']
    ord = numbers.split(',')
    [int(i) for i in ord]
    sort = sorted(ord)
    return HttpResponse(str(sort), content_type="application/json")


def hi2(request):
    numbers = request.GET['numbers'].split(',')
    [int(i) for i in numbers]
    sort = sorted(numbers)
    data = {
        "status": "ok",
        "numbers" : sort,
        "message": "integers sorted"
    }
    print(data)
    return HttpResponse(json.dumps(data), content_type="application/json")


def hi3(request,nombre,edad):
    if edad<12:
        message = "sorry {}".format(nombre)
    else:
        message = "hello {}".format(nombre)
    return HttpResponse(message)