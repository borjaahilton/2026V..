import uuid

from django.db import models
from frejolito.models import Persona


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, unique=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria_padre = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategorias')

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, unique=True)
    pais_origen = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    ruc = models.CharField(max_length=11, unique=True)
    estado = models.BooleanField(default=True)
    tipo_proveedor = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Proveedor: {self.ruc}"

class Descuento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_fin = models.DateTimeField()
    estado = models.BooleanField(default=True)
    codigo_cupon = models.CharField(max_length=50, unique=True, blank=True, null=True)
     
    def __str__(self):
        return f"Descuento {self.porcentaje}% - Código: {self.codigo_cupon}"
    
class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



class Carrito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="activo")
    total_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    

    def __str__(self):
        return f"Carrito de {self.persona}"
    


class DetalleCarrito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        unique_together = ("carrito", "producto")

    def __str__(self):
        return f"{self.producto} x {self.cantidad}"


class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default="pendiente")

    def __str__(self):
        return f"Pedido {self.id} - {self.persona}"


class DetallePedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ("pedido", "producto")

    def __str__(self):
        return f"{self.producto} x {self.cantidad}"


class Pago(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=50)
    estado_pago = models.CharField(max_length=50, default="completado")

    def __str__(self):
        return f"Pago {self.id} - Pedido {self.pedido.id}"
