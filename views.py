from django.shortcuts import render
from app.forms import ObraForm
from django.shortcuts import redirect, render
from .models import Obra

def index(request):
    return render(request, 'app/index.html')

def actores(request):
    return render(request, 'app/actores.html')

def adminTrab2(request):
    return render(request, 'app/adminTrab2.html')
    
def adminTrabajos(request):
    return render(request, 'app/adminTrabajos.html')
    
def bienvenida(request):
    return render(request, 'app/bienvenida.html')
    
def consultarArtista(request):
    return render(request, 'app/consultarArtista.html')
    
def consultarCuentas(request):
    return render(request, 'app/consultarCuentas.html')
    
def crearCuenta(request):
    return render(request, 'app/crearCuenta.html')
    
def inicio(request):
    return render(request, 'app/inicio.html')
    
def jockerPalida(request):
    return render(request, 'app/jockerPalida.html')
        
def juniorFernandez(request):
    return render(request, 'app/juniorFernandez.html')
        
def llenarDatosUsuario(request):
    return render(request, 'app/llenarDatosUsuario.html')
        
def modificarCuenta(request):
    return render(request, 'app/modificarCuenta.html')
        
def modificarPintura(request):
    return render(request, 'app/modificarPintura.html')
            
def pinturas(request):
    return render(request, 'app/pinturas.html')
            
def preguntasFrecu2(request):
    return render(request, 'app/preguntasFrecu2.html')
            
def preguntasFrecuentes(request):
    return render(request, 'app/preguntasFrecuentes.html')
                
def registro1(request):
    return render(request, 'app/registro1.html')
                
def registroExitoso(request):
    return render(request, 'app/registroExitoso.html')
                    
def subirTrabajos(request):
    return render(request, 'app/subirTrabajos.html')
                    
def validacion2(request):
    return render(request, 'app/validacion2.html')

def llenarDatosSubir(request):
    return render(request, 'app/llenarDatosSubir.html')

def buscador(request):
    misTrabajos= Obra.objects.all()
    datos = {
        'misTrabajos' : misTrabajos
    }

    return render (request, 'app/buscador.html',datos)

def misTrabajos(request):
    datos = {
        'form': ObraForm()
      }
    if request.method == 'POST':
        formulario = ObraForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Obra Subida Correctamente"
    return render(request, 'app/misTrabajos.html')

def modificar(request,id):

    obra = Obra.objects.get(idObra=id)

    datos = {
        'form' : ObraForm(instance=obra)
    }

    if request.method == 'POST':

        formulario = ObraForm(data=request.POST,instance=obra)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos modificados correctamente"

    return render (request, 'app/modificar.html', datos)

def eliminar(request,id):

    obra = Obra.objects.get(idObra=id)
    obra.delete()

    return redirect(to="buscador")