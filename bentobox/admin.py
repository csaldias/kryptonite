from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Categoria
from .models import Contenido

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CategoriasInline(admin.StackedInline):
    model = Categoria
    can_delete = False
    verbose_name_plural = 'categorias'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CategoriasInline, )

class ContenidoAdmin(admin.ModelAdmin):
    list_filter = ('aprobado',)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Contenido, ContenidoAdmin)
