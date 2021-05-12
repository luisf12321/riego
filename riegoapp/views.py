from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def estadisticas(request):
    return render(request, 'riego/estadisticas.html')


@login_required
def calendario(request):
    return render(request,'riego/calendario.html')


@login_required
def sectores(request):
    return render(request,'riego/sectores.html')

