from django.shortcuts import render

# Create your views here.
def Nosotros(request):
    return render(request,'sobre_nosotros/sobre_nosotros.html')