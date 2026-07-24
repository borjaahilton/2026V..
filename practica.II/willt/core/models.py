from django.db import models
from django.contrib.auth.models import User, Permission

class Persona(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    nombres = models.CharField(max_length=150)

    class Meta:
        db_table = 'users_persona'

    def __str__(self):
        return f"{self.nombres} ({self.dni})"

class Icono(models.Model):
    nombre = models.CharField(max_length=50)
    recurso = models.FileField(upload_to='iconos/', null=True, blank=True)

    class Meta:
        db_table = 'users_icono'

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nivel_acceso = models.CharField(max_length=50)
    etiqueta = models.CharField(max_length=50)
    icono = models.ForeignKey(Icono, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'users_rol'

    def __str__(self):
        return f"{self.etiqueta} - Nivel {self.nivel_acceso}"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'users_perfil'

    def __str__(self):
        return self.user.username

class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users_rolpermiso'

    def __str__(self):
        return f"Permiso {self.permiso.codename} para Rol {self.rol.id}"
