from django.urls import path
from . import views 


app_name = 'galeria'

urlpatterns = [

    path('Galeria/', views.Imagenes , name= 'galeria')
]