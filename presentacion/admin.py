from django.contrib import admin

from servicios.models import CategoriaServicio, Servicio

# Register your models here.
class CategoriaServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')

admin.site.register(CategoriaServicio, CategoriaServicioAdmin)
admin.site.register(Servicio, ServicioAdmin)