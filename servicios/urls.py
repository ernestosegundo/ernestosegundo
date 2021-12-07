from django.urls import path

from servicios import views

urlpatterns = [
    path('', views.servicios, name='servicios'),
    path('<int:servicio_id>/', views.servicio, name='servicio'),
    path('categoria/<int:categoria_id>/', views.categorias, name='categoria_servicio'),
]