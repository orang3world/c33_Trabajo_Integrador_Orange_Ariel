from django.urls import path
from . import views
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("crear_productos/", views.crear_productos, name="crear_productos"),
    path("crear_proveedores/", views.crear_proveedores, name="crear_proveedores"),
    path("productos/", views.productos, name="productos"),
    path("proveedores/", views.proveedores, name="proveedores"),
]
