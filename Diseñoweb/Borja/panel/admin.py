from django.contrib import admin
from .models import Permiso, DetallePermiso, Rol, DetalleRol

admin.site.register(Permiso)
admin.site.register(DetallePermiso)
admin.site.register(Rol)
admin.site.register(DetalleRol)
