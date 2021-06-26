from django.shortcuts import render

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
        
def misTrabajos(request):
    return render(request, 'app/misTrabajos.html')
        
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

