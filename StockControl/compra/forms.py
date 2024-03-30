from django import forms
from django.forms import ModelForm
from .models import Proveedor, Producto

class ProductoForm(ModelForm):
    nombre = forms.CharField()
    precio = forms.FloatField()
    stock_actual = forms.IntegerField()
    proveedor = forms.ChoiceField()
    #proveedor = forms.ChoiceField(
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual','proveedor']
    
class ProveedorForm(ModelForm):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']
