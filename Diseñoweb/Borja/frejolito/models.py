from django.db import models
from django.contrib.auth.models import User 

class Persona(models.Model):
    # Relación uno a uno con el usuario de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE) 
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.dni}"