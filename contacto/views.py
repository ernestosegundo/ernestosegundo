from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

from contacto.forms import FormularioContacto

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje de sitio web Ernesto Segundo", 
                    "El usuario {} ({}) dice:\n\n {}".format(nombre, email, contenido),
                    "", ["rsernesto@gmail.com"], reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, 'contacto/contacto.html', {"formulario_contacto": formulario_contacto})