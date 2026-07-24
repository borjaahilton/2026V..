# pyrefly: ignore [missing-import]
from rest_framework import viewsets
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
# pyrefly: ignore [missing-import]
from .serializers import (
    PersonaSerializer,
    CategoriaSerializer,
    MarcaSerializer,
    ProveedorSerializer,
    DescuentoSerializer,
    ProductoSerializer,
    CarritoSerializer,
    DetalleCarritoSerializer,
    PedidoSerializer,
    DetallePedidoSerializer,
    PagoSerializer
)

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer


class DetalleCarritoViewSet(viewsets.ModelViewSet):
    queryset = DetalleCarrito.objects.all()
    serializer_class = DetalleCarritoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
