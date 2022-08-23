from django.shortcuts import render

# Create your views here.
def Galeria(request):
    return render(request,'galeria/galeria.html')