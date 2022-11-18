from django.shortcuts import render
from django.http import JsonResponse
from .models import usuariosAnfibio

# Create your views here.
def infoUsuarios(request):
    usuarios_totales = usuariosAnfibio.objects.all()
    usuarios_enviar = []
    for usuario in usuarios_totales:
        usr_datos = [usuario.nombre,usuario.apellido,usuario.codigoUsr]
        usuarios_enviar.append(usr_datos)
    return JsonResponse({
        'usuarios':usuarios_enviar,
    })

def crearUsuario(request):
    nombreUsr = request.GET.get('nombre')
    apelllidoUsr = request.GET.get('apellido')
    celularUsr = request.GET.get('celular')
    emailUsr = request.GET.get('email')
    contraUsr = request.GET.get('contra')
    print(nombreUsr)
    print(apelllidoUsr)
    print(celularUsr)
    print(emailUsr)
    print(contraUsr)
    usuariosAnfibio(nombre=nombreUsr,apellido=apelllidoUsr,nroCelular=celularUsr,email=emailUsr,contra=contraUsr).save()
    return JsonResponse({
        'respuesta':'Ok',
    })

def accederUsuario(request):
    usrNombre = request.GET.get('username')
    usrContra = request.GET.get('contra')
    usuarios_totales = usuariosAnfibio.objects.all()
    acceso_usuario = '0'
    for usuario in usuarios_totales:
        if usuario.nombre == usrNombre:
            if usuario.contra == usrContra:
                acceso_usuario = '1'
    if acceso_usuario == '1':
        return JsonResponse({
            'resp':'200'
        })
    else:
        return JsonResponse({
            'resp':'100'
        })