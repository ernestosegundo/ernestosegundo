from django.urls import path

from presentacion import views

urlpatterns = [
    path('', views.presentacion, name='presentacion'),
]