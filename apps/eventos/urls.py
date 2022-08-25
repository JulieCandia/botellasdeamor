from django.urls import path
from . import views 

app_name = 'eventos'

urlpatterns = [
    
    path('Evento/', views.MostarEventos , name= 'eventos')
]