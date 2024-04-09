from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Producto, Proveedor
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
context = {
    "navbar": "navbar.html",
    "sidebar": "sidebar.html",
    "content": "content.html",
    "subcontent": "index.html",
    "footer": "footer.html",
    "base": "base.html",
}


def inicio(request):
    return render(request, "base.html", context)


def crear_productos(request):
        if request.method == "POST":
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
            return productos(request)
        else:
            form = ProductoForm()
        context["form"] = ProductoForm
        context["subcontent"] = "prod_form.html"

        return render(request, "prod_form.html", context)
    
def crear_proveedores(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
        return proveedores(request)
    else:
        form = ProveedorForm()
    context["form"] = ProveedorForm
    context["subcontent"] = "prov_form.html"
    return render(request, "prov_form.html", context)


def productos(request):
    link_crear='/crear_productos/'
    productos = Producto.objects.all()
    context["productos"] = productos
    context["subcontent"] = "productos.html"
    context["link_crear"] = link_crear
    return render(request, "productos.html", context)


def proveedores(request):
    link_crear = "/crear_proveedores/"
    proveedores = Proveedor.objects.all()
    context["proveedores"] = proveedores
    context["subcontent"] = "proveedores.html"
    context["link_crear"] = link_crear
    return render(request, "proveedores.html", context)
