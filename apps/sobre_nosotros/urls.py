from django.urls import path , include
from . import views 

app_name = 'sobre_nosotros'

urlpatterns = [

    path('SobreNosotros/', views.Nosotros , name= 'sobre_nosotros')
]