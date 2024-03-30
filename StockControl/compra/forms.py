import attrs
from django import forms
from django.forms import ModelForm
from .models import Proveedor, Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual','proveedor']
    
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            'stock_actual':forms.TextInput(attrs={'class':'form-control'}),
            'proveedor':forms.Select(attrs={'class':'form-select'})
        }
class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']
        
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'dni':forms.TextInput(attrs={'class':'form-control'})
        }