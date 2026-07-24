from django.contrib import admin

# pyrefly: ignore [missing-import]
from .models import Persona, Icono, Rol, Perfil, RolPermiso

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombres')

@admin.register(Icono)
class IconoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('etiqueta', 'nivel_acceso')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'persona', 'rol')

@admin.register(RolPermiso)
class RolPermisoAdmin(admin.ModelAdmin):
    list_display = ('rol', 'permiso')
