from django.urls import path
from . import views
urlpatterns = [
    path('crear/<str:seccion>/', views.crear, name='crear'),
    #path('crear_proveedor/<str:nombre>/<str:apellido>/<int:dni>', views.crear_proveedor),
    #path('crear_producto/', views.crear_producto),
    path("listar/<str:seccion>/", views.listar, name='listar'),
    path("borrarTodo/<str:seccion>/", views.borrarTodo)
    ]
