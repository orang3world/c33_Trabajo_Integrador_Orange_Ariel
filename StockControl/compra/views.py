from django.shortcuts import render
from .models import Producto, Proveedor

# Create your views here.
""" 
C R U D 
| | | '────> Delete ──> Productos
| | |               ──> Proveedores
| | |
| | '──────> Update ──> Productos
| |                 ──> Proveedores
| |
| '─────X──> Read   ──> Todos los Productos
|                   ──> Todos los Proveedores
|
'───────X──> Create ──> proveedor
                    ──> producto
"""


def creacion_proveedor(request, nombre, apellido, dni):
    nProVeedor = Proveedor.objects.create(
        nombre=nombre, apellido=apellido, dni=dni
    )
    return listado(request, "proveedores")

def creacion_producto(request, nombre, precio, stock_actual, pv_id):
    pV = Proveedor.objects.get(id = pv_id )
    pV.save()
    nProDucto = Producto.objects.create(
        nombre = nombre,
        precio = precio,
        stock_actual = stock_actual,
        proveedor = pV
    )
    return listado(request, "productos")


def listado(request, modelo):
    if modelo == "productos":
        productos = Producto.objects.all()
        return render(request, "listado_productos.html", {"productos": productos})
    elif modelo == "proveedores":
        proveedores = Proveedor.objects.all()
        return render(request, "listado_proveedores.html", {"proveedores": proveedores})
