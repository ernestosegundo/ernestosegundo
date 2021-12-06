from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm'}))
    email = forms.EmailField(label="Correo Electrónico", required=True, widget=forms.TextInput(attrs={'class': 'form-control input-sm'}))
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea(attrs={'class': 'form-control input-sm'}), required=False)