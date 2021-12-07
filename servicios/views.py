from django.shortcuts import render

from servicios.models import CategoriaServicio, Servicio

# Create your views here.
def servicios(request):
    servicios = Servicio.objects.all()

    return render(request, 'servicios/servicios.html', {"servicios": servicios})

def servicio(request, servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)

    return render(request, 'servicios/servicioid.html', {"servicio": servicio})

def categorias(request, categoria_id):
    categoria_servicio = CategoriaServicio.objects.get(id=categoria_id)

    servicios = Servicio.objects.filter(categoria=categoria_servicio)

    return render(request, 'servicios/categoria.html', {"categoria": categoria_servicio, "servicios": servicios})