from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='crear'),
    path('crear/<str:seccion>/', views.crear, name='crear'),
    path("listar/<str:seccion>/", views.listar, name='listar')
    ]
