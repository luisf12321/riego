import json

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    return render(request, "index.html")


def setting_count(request):
    return render(request, "user/setting.html")