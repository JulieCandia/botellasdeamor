from django.shortcuts import render


# Create your views here.

def Noticias(request):
    return render(request, 'noticias/listar_noticias.html')