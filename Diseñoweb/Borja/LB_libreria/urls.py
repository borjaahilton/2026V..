from django.urls import path
from .views import home_view, validar
from .views import dashboard


urlpatterns = [
    path('inicio/', home_view, name='home'),
    path('validar/', validar, name='validar'),
    path('dashboard/', dashboard, name='dashboard'),
]
