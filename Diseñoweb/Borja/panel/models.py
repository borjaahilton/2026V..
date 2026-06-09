from django.db import models
import uuid
from frejolito.models import Persona

class Permiso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Relación con Persona: Un permiso pertenece a una persona
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="permisos")
    nombre_permiso = models.CharField(max_length=100, default="General")
    estado = models.BooleanField(default=True)
    nivel_acceso = models.IntegerField(default=1)

    def __str__(self):
        return f"Permiso: {self.nombre_permiso}"


class DetallePermiso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE, related_name="detalles")
    es_activo = models.BooleanField(default=True)
    modulo_sistema = models.CharField(max_length=100, blank=True, null=True)
    puede_leer = models.BooleanField(default=True)

    def __str__(self):
        return f"Detalle de {self.permiso.nombre_permiso}"


class Rol(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="roles")
    estado = models.BooleanField(default=True)
    permisos_asignados = models.ManyToManyField(Permiso, related_name="roles_asociados", blank=True)

    class Meta:
        # Ejemplo: El nombre del rol debe ser único para esa persona
        unique_together = ("nombre", "persona")

    def __str__(self):
        return self.nombre


class DetalleRol(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rol = models.OneToOneField(Rol, on_delete=models.CASCADE, related_name="detalle_rol")
    fecha_asignacion = models.DateField(auto_now_add=True)
    asignado_por = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True, related_name="roles_dados")
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Configuración de {self.rol.nombre}"