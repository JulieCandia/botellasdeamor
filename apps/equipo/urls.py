from django.urls import path
from . import views 

app_name = 'equipo'

urlpatterns = [

    path('Equipo/', views.Presentacion , name= 'equipo')
]