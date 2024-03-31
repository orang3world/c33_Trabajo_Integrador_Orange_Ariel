from django.db import models
from django.forms import ModelForm

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    
    def __str__(self):
        return f'{str(self.id)} - {self.nombre}, {self.apellido}'


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor,  on_delete=models.CASCADE)

    