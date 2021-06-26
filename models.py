from django.db import models

class Obras(models.Model):

    id =models.IntegerField(primary_key=True, verbose_name="Id de Obras")
    nombre =models.CharField(max_length=50, verbose_name="Nombre Obras")
    descripcion =models.CharField(max_length=50, verbose_name="Nombre Obras")
    precio =models.IntegerField(verbose_name="Precio obras")

    class Meta:
        db_table = 'obras'

    def str(self):
        return self.idObra

class Obra(models.Model):
    idObra = models.IntegerField(primary_key=True, verbose_name='Id Obras')
    nombre_obra = models.CharField(max_length=100, verbose_name='Nombre de la Obra')
    autor_obra = models.CharField(max_length=100, null=True, verbose_name='Autor')
    precio = models.IntegerField(verbose_name='Valor de la Obra')

    class Meta:
        db_table = 'obra'

    def str(self):
        return self.nombre_obra

