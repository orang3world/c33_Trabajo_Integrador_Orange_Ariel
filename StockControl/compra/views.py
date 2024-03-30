from django.shortcuts import render

from .models import Producto, Proveedor
from django.http import HttpResponseRedirect
from .forms import ProductoForm, ProveedorForm


# Create your views here.
""" 
C R U D 
| | | '─X──> Delete ──> Productos
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

'''
def crear_proveedor(request, nombre, apellido, dni):
    nProVeedor = Proveedor.objects.create(
        nombre=nombre, apellido=apellido, dni=dni
    )
    return listar(request, "proveedores")

def crear_producto(request, form):
    pV = Proveedor.objects.get(id = form.pv_id )
    pV.save()
    nProDucto = Producto.objects.create(
        nombre = form.nombre,
        precio = form.precio,
        stock_actual = form.stock_actual,
        proveedor = pV
    )
    return listar(request, "productos")
'''


def crear(request, seccion):
    if seccion == "productos":
        if request.method == "POST":
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
            return listar(request, seccion)
        else:
            form = ProductoForm()
        return render(request, "prod_form.html", {"form": ProductoForm})
    elif seccion == "proveedores":
        if request.method == "POST":
            form = ProveedorForm(request.POST)
            if form.is_valid():
                form.save()
            return listar(request, seccion)
        else:
            form = ProveedorForm()
        return render(request, "prov_form.html", {"form": ProveedorForm})


def listar(request, seccion):
    if seccion == "productos":
        productos = Producto.objects.all()
        return render(request, "listar_productos.html", {"productos": productos})
    elif seccion == "proveedores":
        proveedores = Proveedor.objects.all()
        return render(request, "listar_proveedores.html", {"proveedores": proveedores})


def borrarTodo(request, seccion):
    if seccion == "productos":
        productos = Producto.objects.all()
        productos.delete()
        return render(request, "listar_productos.html", {"productos": productos})
    elif seccion == "proveedores":
        proveedores = Proveedor.objects.all()
        proveedores.delete()
        return render(request, "listar_proveedores.html", {"proveedores": proveedores})