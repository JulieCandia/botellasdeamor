from django.urls import path
from . import views 

app_name = 'contacto'

urlpatterns = [

    path('Contacto/', views.Contacto , name= 'contacto')
]