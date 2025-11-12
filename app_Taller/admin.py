# app_Taller/admin.py
from django.contrib import admin
from .models import Cliente, Vehiculo, Personal, Proveedor, Refaccion, Servicio, Orden, DetalleOrden

admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Personal)
admin.site.register(Proveedor)
admin.site.register(Refaccion)
admin.site.register(Servicio)
admin.site.register(Orden)
admin.site.register(DetalleOrden)