from django.db import models

class Obra(models.Model):

    idObra =models.IntegerField(primary_key=True, verbose_name="Id de Obras")
    nombre =models.CharField(max_length=50, verbose_name="Nombre Obras")
    descripcion =models.CharField(max_length=200, verbose_name="Nombre Obras")
    precio =models.IntegerField(verbose_name="Precio obras")

    def str(self):
        return self.idObra



