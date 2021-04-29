from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

users = [
    {
        "nombre":"luis",
        "user":"luisf124321",
        "time": datetime.now()

    },
    {
        "nombre":"juan",
        "user":"juan124321",
        "time": datetime.now()

    },
    {
        "nombre":"pedro",
        "user":"pedro124321",
        "time": datetime.now()
    }
]

def list_usuario(request):
    #usuarios = [1,2,3]
    content = []
    for usuario in users:
        content.append("""
        <p><strong>{nombre}</strong></p>
        <p><strong>{user}</strong></p>
        <p><strong>{time}</strong></p>
        """.format(**usuario))
    return HttpResponse('<br>'.join(content))


def usuarios(request):
    return  render(request, 'feed.html', {"nombre":"luis fer", "usuarios": users })