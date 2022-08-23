from django.urls import path
from . import views 

app_name = 'equipo'

urlpatterns = [

    path('Equipo/', views.Equipo , name= 'equipo')
]