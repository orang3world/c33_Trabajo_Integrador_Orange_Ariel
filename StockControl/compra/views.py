from django.shortcuts import render
from .models import Producto, Proveedor

# Create your views here.
''' 
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
'''

def creacion_proveedor(request, nombre, apellido, dni):
        nuevo_proveedor = Proveedor.objects.create(
        nombre = nombre,
        apellido = apellido,
        dni = dni
        )
        return render(request, 'listado_proveedores.html', {'modelo':'proveedores'})


def creacion_producto(request, nombre, precio, stock_actual, proveedor):
        nuevo_producto = Producto.objects.create(
        nombre = nombre,
        precio = precio,
        stock_actual = stock_actual,
        proveedor = proveedor
        )
        return render(request, 'listado_productos.html', {'modelo':'productos'})

def listado(request, modelo):
    if modelo == 'productos':
        productos = Producto.objects.all()
        return render(request, 'listado_productos.html', {'productos':productos})
    elif modelo == 'proveedores':
        proveedores = Proveedor.objects.all()
        return render(request, 'listado_proveedores.html', {'proveedores':proveedores})


