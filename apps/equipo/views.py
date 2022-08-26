from django.shortcuts import render
from .models import Equipo

# Create your views here

def Presentacion(request):
    ctx = {}
    todas = Equipo.objects.all()
    ctx['equipo'] = todas 

    return render(request,'equipo/equipo.html', ctx)
