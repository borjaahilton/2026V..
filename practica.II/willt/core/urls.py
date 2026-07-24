from django.urls import path
# pyrefly: ignore [missing-import]
from . import views
 
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('user/', views.user_dashboard, name='user_dashboard'),
]