
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio),
    path('compra/', views.compra),
    path('pago/', views.pago),
]
