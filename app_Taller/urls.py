# app_Taller/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio_taller, name='inicio_taller'),

    # URLs de Cliente
    path('clientes/', views.ver_cliente, name='ver_cliente'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),

    # URLs de Vehiculo
    path('vehiculos/', views.ver_vehiculo, name='ver_vehiculo'),
    path('vehiculos/agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculos/actualizar/<int:pk>/', views.actualizar_vehiculo, name='actualizar_vehiculo'),
    path('vehiculos/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_vehiculo, name='realizar_actualizacion_vehiculo'),
    path('vehiculos/borrar/<int:pk>/', views.borrar_vehiculo, name='borrar_vehiculo'),

    # URLs de Personal
    path('personal/', views.ver_personal, name='ver_personal'),
    path('personal/agregar/', views.agregar_personal, name='agregar_personal'),
    path('personal/actualizar/<int:pk>/', views.actualizar_personal, name='actualizar_personal'),
    path('personal/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_personal, name='realizar_actualizacion_personal'),
    path('personal/borrar/<int:pk>/', views.borrar_personal, name='borrar_personal'),

    # URLs de Proveedor
    path('proveedores/', views.ver_proveedor, name='ver_proveedor'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/actualizar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedores/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),

    # URLs de Refaccion
    path('refacciones/', views.ver_refaccion, name='ver_refaccion'),
    path('refacciones/agregar/', views.agregar_refaccion, name='agregar_refaccion'),
    path('refacciones/actualizar/<int:pk>/', views.actualizar_refaccion, name='actualizar_refaccion'),
    path('refacciones/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_refaccion, name='realizar_actualizacion_refaccion'),
    path('refacciones/borrar/<int:pk>/', views.borrar_refaccion, name='borrar_refaccion'),

    # URLs de Servicio
    path('servicios/', views.ver_servicio, name='ver_servicio'),
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/actualizar/<int:pk>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('servicios/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_servicio, name='realizar_actualizacion_servicio'),
    path('servicios/borrar/<int:pk>/', views.borrar_servicio, name='borrar_servicio'),

    # URLs de Orden
    path('ordenes/', views.ver_orden, name='ver_orden'),
    path('ordenes/agregar/', views.agregar_orden, name='agregar_orden'),
    path('ordenes/actualizar/<int:pk>/', views.actualizar_orden, name='actualizar_orden'),
    path('ordenes/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_orden, name='realizar_actualizacion_orden'),
    path('ordenes/borrar/<int:pk>/', views.borrar_orden, name='borrar_orden'),

    # URLs de DetalleOrden
    path('detalleordenes/', views.ver_detalleorden, name='ver_detalleorden'),
    path('detalleordenes/agregar/', views.agregar_detalleorden, name='agregar_detalleorden'),
    path('detalleordenes/actualizar/<int:pk>/', views.actualizar_detalleorden, name='actualizar_detalleorden'),
    path('detalleordenes/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_detalleorden, name='realizar_actualizacion_detalleorden'),
    path('detalleordenes/borrar/<int:pk>/', views.borrar_detalleorden, name='borrar_detalleorden'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)