from django.urls import path
from . import views
urlpatterns = [
    path('crear/proveedor/<str:nombre>/<str:apellido>/<int:dni>', views.crear_proveedor),
    path('crear/producto/<str:nombre>/<str:precio>/<int:stock_actual>/<int:pv_id>/', views.crear_producto),
    path("listar/<str:seccion>/", views.listar),
    path("borrarTodo/<str:seccion>/", views.borrarTodo)
    ]
