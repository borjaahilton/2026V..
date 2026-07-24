from django.urls import path, include
# pyrefly: ignore [missing-import]
from rest_framework.routers import DefaultRouter
# pyrefly: ignore [missing-import]
from . import views
# pyrefly: ignore [missing-import]
from .api_views import (
    PersonaViewSet,
    CategoriaViewSet,
    MarcaViewSet,
    ProveedorViewSet,
    DescuentoViewSet,
    ProductoViewSet,
    CarritoViewSet,
    DetalleCarritoViewSet,
    PedidoViewSet,
    DetallePedidoViewSet,
    PagoViewSet
)

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'descuentos', DescuentoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'carritos', CarritoViewSet)
router.register(r'detalles-carrito', DetalleCarritoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'detalles-pedido', DetallePedidoViewSet)
router.register(r'pagos', PagoViewSet)

urlpatterns = [
    path('', views.index, name='backed_index'),
    path('ejemplo/', views.ejemplo_api, name='ejemplo_api'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_confirm/', views.reset_password_confirm, name='reset_password_confirm'),  
    path('Bck/', include(router.urls)),
]

