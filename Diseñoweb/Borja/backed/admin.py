from django.contrib import admin
from .models import (
    Producto, Categoria, Marca, Proveedor, Descuento,
    Carrito, DetalleCarrito, Pedido, DetallePedido, Pago
)

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Proveedor)
admin.site.register(Descuento)
admin.site.register(Carrito)
admin.site.register(DetalleCarrito)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Pago)
