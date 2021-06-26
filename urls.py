from django.urls import path
from .views import index, inicio, jockerPalida, juniorFernandez, llenarDatosSubir, llenarDatosUsuario, misTrabajos, modificarCuenta, modificarPintura, pinturas, preguntasFrecu2, preguntasFrecuentes, registro1, registroExitoso, subirTrabajos, validacion2, actores, adminTrab2, adminTrabajos, bienvenida, consultarArtista, consultarCuentas, crearCuenta

urlpatterns = [
    path('', index, name="index"),
    path('inicio/', inicio, name="inicio"),
    path('jockerPalida/', jockerPalida, name="jockerPalida"),
    path('juniorFernandez/', juniorFernandez, name="juniorFernandez"),
    path('llenarDatosSubir/', llenarDatosSubir, name="llenarDatosSubir"),
    path('llenarDatosUsuario/', llenarDatosUsuario, name="llenarDatosUsuario"),
    path('misTrabajos/', misTrabajos, name="misTrabajos"),
    path('modificarCuenta/', modificarCuenta, name="modificarCuenta"),
    path('modificarPintura/', modificarPintura, name="modificarPintura"),
    path('pinturas/', pinturas, name="pinturas"),
    path('preguntasFrecu2/', preguntasFrecu2, name="preguntasFrecu2"),
    path('preguntasFrecuentes/', preguntasFrecuentes, name="preguntasFrecuentes"),
    path('registro1/', registro1, name="registro1"),
    path('registroExitoso/', registroExitoso, name="registroExitoso"),
    path('subirTrabajos/', subirTrabajos, name="subirTrabajos"),
    path('validacion2/', validacion2, name="validacion2"),
    path('actores/', actores, name="actores"),
    path('adminTrab2/', adminTrab2, name="adminTrab2"),
    path('adminTrabajos/', adminTrabajos, name="adminTrabajos"),
    path('bienvenida/', bienvenida, name="bienvenida"),
    path('consultarArtista/', consultarArtista, name="consultarArtista"),
    path('consultarCuentas/', consultarCuentas, name="consultarCuentas"),
    path('crearCuenta/', crearCuenta, name="crearCuenta"),
]