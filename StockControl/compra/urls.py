from django.urls import path
from . import views
urlpatterns = [
    path("listado/creacion_proveedor/<str:nombre>/<str:apellido>/<int:dni>", views.creacion_proveedor),
    path("listado/creacion_producto/<str:nombre>/<str:precio>/<int:stock_actual>/<int:pv_id>/", views.creacion_producto),
    #path("listado/nuevo_producto/<str:nombre>/<int:precio>/<int:stock_actual>/<str:proveedor>/", views.creacion_producto),
    path("listado/<str:modelo>/", views.listado),
    path("borradoTotal/<str:modelo>/", views.borradoTotal)
    #path("listado/proveedores/", views.listado)
    ]
