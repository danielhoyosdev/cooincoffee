from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cooperativa(models.Model):
    nit         = models.CharField(max_length = 15, unique = True)
    nombre      = models.CharField(max_length = 50)
    ciudad      = models.CharField(max_length = 20)
    direccion   = models.CharField(max_length = 100)
    telefono    = models.IntegerField(null = True, blank = True)
    logo        = models.ImageField(upload_to = "cooperativas", null = True, blank = True)
    estado      = models.BooleanField(default = True)

    def __str__ (self):
        return self.nombre

class Asociado(models.Model):
    documento   = models.CharField(max_length = 15, unique = True)
    nombre      = models.CharField(max_length = 30)
    apellido    = models.CharField(max_length = 30)
    direccion   = models.CharField(max_length = 100, null = True, blank = True)
    telefono    = models.CharField(max_length = 15, null = True, blank = True)
    estado      = models.BooleanField(default = True)

    def __str__ (self):
        return self.nombre

class TipoCafe(models.Model):
    nombre = models.CharField(max_length = 50, unique = True)

    def __str__ (self):
        return self.nombre

class Factura(models.Model):
    codigo        = models.CharField(max_length = 10, unique = True)
    fechaRegistro = models.DateField()
    cooperativa   = models.ForeignKey(Cooperativa, on_delete = models.PROTECT)
    usuario       = models.ForeignKey(User, on_delete = models.PROTECT)

class DetalleFactura(models.Model):
    cantidad    = models.IntegerField()
    unidad      = models.CharField(max_length = 10, default = 'Kilo')
    valorTotal  = models.IntegerField()
    idTipoCafe  = models.ForeignKey(TipoCafe, on_delete = models.PROTECT)
    idAsociado  = models.ForeignKey(Asociado, on_delete = models.PROTECT)
    idFactura   = models.ForeignKey(Factura, on_delete = models.PROTECT)

    def valorUnitario(self):
        valor = self.valorTotal // self.cantidad
        return valor