from django.urls import path

from .views import  DetallePost , Noticias , Listado

app_name = 'noticias'

urlpatterns = [
    
    path('Noticias/', Noticias.as_view(), name = 'noticias'),
    path('ListadoEducacion/',Listado.as_view(),{'nombre':'Educacion'}, name='educacion'),
    path('ListadoGeneral/',Listado.as_view(),{'nombre':'General'}, name='general'),
    path('ListadoInformativo/',Listado.as_view(),{'nombre':'Informativo'}, name='informativo'),
    path('<slug:slug>',DetallePost.as_view(),name='detalle_post')
]