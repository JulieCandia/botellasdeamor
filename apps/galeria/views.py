from django.shortcuts import render
from .models import Categoria, Galeria
# Create your views here.

# def Categoria(request):
#     context = {}

#     todas = Categoria.objects.all()

#     context['categoria'] = todas

#     return render(request,'galeria/galeria.html', context)

def Imagenes(request):
    ctx = {}

    todo = Galeria.objects.all()

    ctx['imagenes'] = todo

    return render(request,'galeria/galeria.html', ctx )