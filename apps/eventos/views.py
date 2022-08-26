from django.shortcuts import render
from .models import Evento
# Create your views here.

def MostarEventos(request):
    ctx = {}
    todos = Evento.objects.all().order_by("fecha")
    ctx['eventos'] = todos

    return render(request,'eventos/eventos.html', ctx)