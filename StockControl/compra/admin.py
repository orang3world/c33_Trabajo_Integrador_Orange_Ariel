from tabnanny import verbose
from django.contrib import admin

from .models import Producto, Proveedor

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio','stock_actual', 'proveedor_id']
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','dni']


# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)