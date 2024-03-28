from django.shortcuts import render
from .models import Producto, Proveedor
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm, generalForm

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


def crear_proveedor(request, nombre, apellido, dni):
    nProVeedor = Proveedor.objects.create(
        nombre=nombre, apellido=apellido, dni=dni
    )
    return listar(request, "proveedores")

def crear_producto(request, nombre, precio, stock_actual, pv_id):
    pV = Proveedor.objects.get(id = pv_id )
    pV.save()
    nProDucto = Producto.objects.create(
        nombre = nombre,
        precio = precio,
        stock_actual = stock_actual,
        proveedor = pV
    )
    return listar(request, "productos")


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



def generalFormView(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = generalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")
    return render(request, "form.html", {"form": form})