from django.contrib import admin

from blog.models import CategoriaPost, Post

# Register your models here.
class CategoriaPostAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')

admin.site.register(CategoriaPost, CategoriaPostAdmin)
admin.site.register(Post, PostAdmin)