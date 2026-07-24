import uuid
# pyrefly: ignore [missing-import]
from rest_framework import serializers
from frejolito.models import Persona
# pyrefly: ignore [missing-import]
from .models import (
    Categoria,
    Marca,
    Proveedor,
    Descuento,
    Producto,
    Carrito,
    DetalleCarrito,
    Pedido,
    DetallePedido,
    Pago
)

# Serializador para el modelo auxiliar Persona
class PersonaSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='usuario.username', read_only=True)
    email = serializers.CharField(source='usuario.email', read_only=True)

    class Meta:
        model = Persona
        fields = ['id', 'usuario', 'username', 'email', 'dni', 'telefono', 'direccion', 'es_activo']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    persona_detalles = PersonaSerializer(source='id_persona', read_only=True)

    class Meta:
        model = Proveedor
        fields = ['id', 'id_persona', 'persona_detalles', 'ruc', 'estado', 'tipo_proveedor']


class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    proveedor_ruc = serializers.CharField(source='proveedor.ruc', read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'categoria', 'categoria_nombre', 'proveedor', 'proveedor_ruc']


class DetalleCarritoSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_precio = serializers.DecimalField(source='producto.precio', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = DetalleCarrito
        fields = ['id', 'carrito', 'producto', 'producto_nombre', 'producto_precio', 'cantidad', 'subtotal']


class CarritoSerializer(serializers.ModelSerializer):
    detalles = DetalleCarritoSerializer(source='detallecarrito_set', many=True, read_only=True)
    persona_nombre = serializers.CharField(source='persona.usuario.username', read_only=True)

    class Meta:
        model = Carrito
        fields = ['id', 'persona', 'persona_nombre', 'creado', 'estado', 'total_estimado', 'detalles']


class DetallePedidoSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = DetallePedido
        fields = ['id', 'pedido', 'producto', 'producto_nombre', 'cantidad', 'precio']


class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(source='detallepedido_set', many=True, read_only=True)
    persona_nombre = serializers.CharField(source='persona.usuario.username', read_only=True)

    class Meta:
        model = Pedido
        fields = ['id', 'persona', 'persona_nombre', 'fecha', 'total', 'estado', 'detalles']


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'
