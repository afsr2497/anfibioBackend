from . import views
from django.urls import path

app_name='infoAnfibio'

urlpatterns = [
    path('infoUsuarios',views.infoUsuarios,name='infoUsuarios'),
    path('crearUsuario',views.crearUsuario,name='crearUsuario'),
    path('accederUsuario',views.accederUsuario,name='accederUsuario')
]