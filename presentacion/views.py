from django.shortcuts import render

# Create your views here.
def presentacion(request):
    return render(request, 'presentacion/presentacion.html')