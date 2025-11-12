# app_Taller/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Vehiculo, Personal, Proveedor, Refaccion, Servicio, Orden, DetalleOrden
from django.db.models import Q # Para la barra de búsqueda

# ==========================================
# VISTAS GENERALES
# ==========================================

def inicio_taller(request):
    return render(request, 'inicio.html')

# ==========================================
# VISTAS DE CLIENTE
# ==========================================

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        email = request.POST['email']
        rfc = request.POST['rfc']
        direccion = request.POST['direccion']
        imagen = request.FILES.get('imagen')

        cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono,
                          email=email, rfc=rfc, direccion=direccion, imagen=imagen)
        cliente.save()
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')

def ver_cliente(request):
    query = request.GET.get('q')
    if query:
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(email__icontains=query) |
            Q(rfc__icontains=query)
        ).order_by('nombre')
    else:
        clientes = Cliente.objects.all().order_by('nombre')
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, pk):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.rfc = request.POST['rfc']
        cliente.direccion = request.POST['direccion']
        if 'imagen' in request.FILES:
            cliente.imagen = request.FILES['imagen']
        cliente.save()
        return redirect('ver_cliente')
    return redirect('ver_cliente')

def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})


# ==========================================
# VISTAS DE VEHICULO
# ==========================================

def agregar_vehiculo(request):
    clientes = Cliente.objects.all().order_by('nombre')
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        matricula = request.POST['matricula']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        anio = request.POST['anio']
        kilometraje = request.POST['kilometraje']
        imagen = request.FILES.get('imagen')

        vehiculo = Vehiculo(cliente=cliente, matricula=matricula, marca=marca,
                            modelo=modelo, anio=anio, kilometraje=kilometraje, imagen=imagen)
        vehiculo.save()
        return redirect('ver_vehiculo')
    return render(request, 'vehiculo/agregar_vehiculo.html', {'clientes': clientes})

def ver_vehiculo(request):
    query = request.GET.get('q')
    if query:
        vehiculos = Vehiculo.objects.filter(
            Q(matricula__icontains=query) |
            Q(marca__icontains=query) |
            Q(modelo__icontains=query) |
            Q(cliente__nombre__icontains=query) |
            Q(cliente__apellido__icontains=query)
        ).order_by('marca')
    else:
        vehiculos = Vehiculo.objects.all().order_by('marca')
    return render(request, 'vehiculo/ver_vehiculo.html', {'vehiculos': vehiculos})

def actualizar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    clientes = Cliente.objects.all().order_by('nombre')
    return render(request, 'vehiculo/actualizar_vehiculo.html', {'vehiculo': vehiculo, 'clientes': clientes})

def realizar_actualizacion_vehiculo(request, pk):
    if request.method == 'POST':
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        cliente_id = request.POST['cliente']
        vehiculo.cliente = get_object_or_404(Cliente, pk=cliente_id)
        vehiculo.matricula = request.POST['matricula']
        vehiculo.marca = request.POST['marca']
        vehiculo.modelo = request.POST['modelo']
        vehiculo.anio = request.POST['anio']
        vehiculo.kilometraje = request.POST['kilometraje']
        if 'imagen' in request.FILES:
            vehiculo.imagen = request.FILES['imagen']
        vehiculo.save()
        return redirect('ver_vehiculo')
    return redirect('ver_vehiculo')

def borrar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('ver_vehiculo')
    return render(request, 'vehiculo/borrar_vehiculo.html', {'vehiculo': vehiculo})


# ==========================================
# VISTAS DE PERSONAL
# ==========================================

def agregar_personal(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        cargo = request.POST['cargo']
        fecha_contratacion = request.POST['fecha_contratacion']
        salario_base = request.POST['salario_base']
        telefono_contacto = request.POST['telefono_contacto']
        imagen = request.FILES.get('imagen')

        personal = Personal(nombre=nombre, apellido=apellido, cargo=cargo,
                            fecha_contratacion=fecha_contratacion,
                            salario_base=salario_base,
                            telefono_contacto=telefono_contacto, imagen=imagen)
        personal.save()
        return redirect('ver_personal')
    return render(request, 'personal/agregar_personal.html')

def ver_personal(request):
    query = request.GET.get('q')
    if query:
        personal_list = Personal.objects.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(cargo__icontains=query) |
            Q(telefono_contacto__icontains=query)
        ).order_by('nombre')
    else:
        personal_list = Personal.objects.all().order_by('nombre')
    return render(request, 'personal/ver_personal.html', {'personal_list': personal_list})

def actualizar_personal(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    return render(request, 'personal/actualizar_personal.html', {'personal': personal})

def realizar_actualizacion_personal(request, pk):
    if request.method == 'POST':
        personal = get_object_or_404(Personal, pk=pk)
        personal.nombre = request.POST['nombre']
        personal.apellido = request.POST['apellido']
        personal.cargo = request.POST['cargo']
        personal.fecha_contratacion = request.POST['fecha_contratacion']
        personal.salario_base = request.POST['salario_base']
        personal.telefono_contacto = request.POST['telefono_contacto']
        if 'imagen' in request.FILES:
            personal.imagen = request.FILES['imagen']
        personal.save()
        return redirect('ver_personal')
    return redirect('ver_personal')

def borrar_personal(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        personal.delete()
        return redirect('ver_personal')
    return render(request, 'personal/borrar_personal.html', {'personal': personal})

# ==========================================
# VISTAS DE PROVEEDOR
# ==========================================

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre_empresa = request.POST['nombre_empresa']
        contacto_nombre = request.POST['contacto_nombre']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']
        rfc_fiscal = request.POST['rfc_fiscal']

        proveedor = Proveedor(nombre_empresa=nombre_empresa, contacto_nombre=contacto_nombre,
                              telefono=telefono, email=email, direccion=direccion,
                              rfc_fiscal=rfc_fiscal)
        proveedor.save()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/agregar_proveedor.html')

def ver_proveedor(request):
    query = request.GET.get('q')
    if query:
        proveedores = Proveedor.objects.filter(
            Q(nombre_empresa__icontains=query) |
            Q(contacto_nombre__icontains=query) |
            Q(email__icontains=query) |
            Q(rfc_fiscal__icontains=query)
        ).order_by('nombre_empresa')
    else:
        proveedores = Proveedor.objects.all().order_by('nombre_empresa')
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})

def actualizar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, pk):
    if request.method == 'POST':
        proveedor = get_object_or_404(Proveedor, pk=pk)
        proveedor.nombre_empresa = request.POST['nombre_empresa']
        proveedor.contacto_nombre = request.POST['contacto_nombre']
        proveedor.telefono = request.POST['telefono']
        proveedor.email = request.POST['email']
        proveedor.direccion = request.POST['direccion']
        proveedor.rfc_fiscal = request.POST['rfc_fiscal']
        proveedor.save()
        return redirect('ver_proveedor')
    return redirect('ver_proveedor')

def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# ==========================================
# VISTAS DE REFACCION
# ==========================================

def agregar_refaccion(request):
    proveedores = Proveedor.objects.all().order_by('nombre_empresa')
    if request.method == 'POST':
        proveedor_id = request.POST['proveedor']
        proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
        nombre = request.POST['nombre']
        referencia = request.POST['referencia']
        stock = request.POST['stock']
        precio_compra = request.POST['precio_compra']

        refaccion = Refaccion(proveedor=proveedor, nombre=nombre, referencia=referencia,
                              stock=stock, precio_compra=precio_compra)
        refaccion.save()
        return redirect('ver_refaccion')
    return render(request, 'refaccion/agregar_refaccion.html', {'proveedores': proveedores})

def ver_refaccion(request):
    query = request.GET.get('q')
    if query:
        refacciones = Refaccion.objects.filter(
            Q(nombre__icontains=query) |
            Q(referencia__icontains=query) |
            Q(proveedor__nombre_empresa__icontains=query)
        ).order_by('nombre')
    else:
        refacciones = Refaccion.objects.all().order_by('nombre')
    return render(request, 'refaccion/ver_refaccion.html', {'refacciones': refacciones})

def actualizar_refaccion(request, pk):
    refaccion = get_object_or_404(Refaccion, pk=pk)
    proveedores = Proveedor.objects.all().order_by('nombre_empresa')
    return render(request, 'refaccion/actualizar_refaccion.html', {'refaccion': refaccion, 'proveedores': proveedores})

def realizar_actualizacion_refaccion(request, pk):
    if request.method == 'POST':
        refaccion = get_object_or_404(Refaccion, pk=pk)
        proveedor_id = request.POST['proveedor']
        refaccion.proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
        refaccion.nombre = request.POST['nombre']
        refaccion.referencia = request.POST['referencia']
        refaccion.stock = request.POST['stock']
        refaccion.precio_compra = request.POST['precio_compra']
        refaccion.save()
        return redirect('ver_refaccion')
    return redirect('ver_refaccion')

def borrar_refaccion(request, pk):
    refaccion = get_object_or_404(Refaccion, pk=pk)
    if request.method == 'POST':
        refaccion.delete()
        return redirect('ver_refaccion')
    return render(request, 'refaccion/borrar_refaccion.html', {'refaccion': refaccion})

# ==========================================
# VISTAS DE SERVICIO
# ==========================================

def agregar_servicio(request):
    if request.method == 'POST':
        nombre_servicio = request.POST['nombre_servicio']
        descripcion = request.POST['descripcion']
        precio_base = request.POST['precio_base']
        tiempo_estimado_horas = request.POST['tiempo_estimado_horas']
        aplica_garantia = request.POST.get('aplica_garantia') == 'on'

        servicio = Servicio(nombre_servicio=nombre_servicio, descripcion=descripcion,
                            precio_base=precio_base, tiempo_estimado_horas=tiempo_estimado_horas,
                            aplica_garantia=aplica_garantia)
        servicio.save()
        return redirect('ver_servicio')
    return render(request, 'servicio/agregar_servicio.html')

def ver_servicio(request):
    query = request.GET.get('q')
    if query:
        servicios = Servicio.objects.filter(
            Q(nombre_servicio__icontains=query) |
            Q(descripcion__icontains=query)
        ).order_by('nombre_servicio')
    else:
        servicios = Servicio.objects.all().order_by('nombre_servicio')
    return render(request, 'servicio/ver_servicio.html', {'servicios': servicios})

def actualizar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    return render(request, 'servicio/actualizar_servicio.html', {'servicio': servicio})

def realizar_actualizacion_servicio(request, pk):
    if request.method == 'POST':
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.nombre_servicio = request.POST['nombre_servicio']
        servicio.descripcion = request.POST['descripcion']
        servicio.precio_base = request.POST['precio_base']
        servicio.tiempo_estimado_horas = request.POST['tiempo_estimado_horas']
        servicio.aplica_garantia = request.POST.get('aplica_garantia') == 'on'
        servicio.save()
        return redirect('ver_servicio')
    return redirect('ver_servicio')

def borrar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('ver_servicio')
    return render(request, 'servicio/borrar_servicio.html', {'servicio': servicio})

# ==========================================
# VISTAS DE ORDEN
# ==========================================

def agregar_orden(request):
    clientes = Cliente.objects.all().order_by('nombre')
    vehiculos = Vehiculo.objects.all().order_by('matricula')
    personal_list = Personal.objects.all().order_by('nombre')

    if request.method == 'POST':
        vehiculo_id = request.POST['vehiculo']
        cliente_id = request.POST['cliente']
        personal_recepcion_id = request.POST['personal_recepcion']
        personal_mecanico_id = request.POST['personal_mecanico']
        fecha_salida_estimada = request.POST['fecha_salida_estimada']
        fecha_salida = request.POST.get('fecha_salida') # Puede ser null
        problema = request.POST['problema']
        testigos_encendidos = request.POST.get('testigos_encendidos') # Puede ser null
        estado = request.POST['estado']

        vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        personal_recepcion = get_object_or_404(Personal, pk=personal_recepcion_id)
        personal_mecanico = get_object_or_404(Personal, pk=personal_mecanico_id)

        orden = Orden(vehiculo=vehiculo, cliente=cliente,
                      personal_recepcion=personal_recepcion,
                      personal_mecanico=personal_mecanico,
                      fecha_salida_estimada=fecha_salida_estimada,
                      fecha_salida=fecha_salida if fecha_salida else None,
                      problema=problema,
                      testigos_encendidos=testigos_encendidos if testigos_encendidos else None,
                      estado=estado)
        orden.save()
        return redirect('ver_orden')
    return render(request, 'orden/agregar_orden.html', {
        'clientes': clientes,
        'vehiculos': vehiculos,
        'personal_list': personal_list
    })

def ver_orden(request):
    query = request.GET.get('q')
    if query:
        ordenes = Orden.objects.filter(
            Q(vehiculo__matricula__icontains=query) |
            Q(cliente__nombre__icontains=query) |
            Q(cliente__apellido__icontains=query) |
            Q(personal_recepcion__nombre__icontains=query) |
            Q(personal_mecanico__nombre__icontains=query) |
            Q(estado__icontains=query)
        ).order_by('-fecha_entrada')
    else:
        ordenes = Orden.objects.all().order_by('-fecha_entrada')
    return render(request, 'orden/ver_orden.html', {'ordenes': ordenes})

def actualizar_orden(request, pk):
    orden = get_object_or_404(Orden, pk=pk)
    clientes = Cliente.objects.all().order_by('nombre')
    vehiculos = Vehiculo.objects.all().order_by('matricula')
    personal_list = Personal.objects.all().order_by('nombre')
    return render(request, 'orden/actualizar_orden.html', {
        'orden': orden,
        'clientes': clientes,
        'vehiculos': vehiculos,
        'personal_list': personal_list
    })

def realizar_actualizacion_orden(request, pk):
    if request.method == 'POST':
        orden = get_object_or_404(Orden, pk=pk)
        vehiculo_id = request.POST['vehiculo']
        cliente_id = request.POST['cliente']
        personal_recepcion_id = request.POST['personal_recepcion']
        personal_mecanico_id = request.POST['personal_mecanico']

        orden.vehiculo = get_object_or_404(Vehiculo, pk=vehiculo_id)
        orden.cliente = get_object_or_404(Cliente, pk=cliente_id)
        orden.personal_recepcion = get_object_or_404(Personal, pk=personal_recepcion_id)
        orden.personal_mecanico = get_object_or_404(Personal, pk=personal_mecanico_id)

        orden.fecha_salida_estimada = request.POST['fecha_salida_estimada']
        fecha_salida = request.POST.get('fecha_salida')
        orden.fecha_salida = fecha_salida if fecha_salida else None
        orden.problema = request.POST['problema']
        testigos_encendidos = request.POST.get('testigos_encendidos')
        orden.testigos_encendidos = testigos_encendidos if testigos_encendidos else None
        orden.estado = request.POST['estado']
        orden.save()
        return redirect('ver_orden')
    return redirect('ver_orden')

def borrar_orden(request, pk):
    orden = get_object_or_404(Orden, pk=pk)
    if request.method == 'POST':
        orden.delete()
        return redirect('ver_orden')
    return render(request, 'orden/borrar_orden.html', {'orden': orden})

# ==========================================
# VISTAS DE DETALLEORDEN
# ==========================================

def agregar_detalleorden(request):
    ordenes = Orden.objects.all().order_by('-fecha_entrada')
    refacciones = Refaccion.objects.all().order_by('nombre')
    servicios = Servicio.objects.all().order_by('nombre_servicio')

    if request.method == 'POST':
        orden_id = request.POST['orden']
        servicio_id = request.POST.get('servicio')
        refaccion_id = request.POST.get('refaccion')
        tipo_cargo = request.POST['tipo_cargo']
        descripcion = request.POST['descripcion']
        cantidad_uni_hr = request.POST['cantidad_uni_hr']
        precio_unitario = request.POST['precio_unitario']
        subtotal = request.POST['subtotal']

        orden = get_object_or_404(Orden, pk=orden_id)
        servicio = get_object_or_404(Servicio, pk=servicio_id) if servicio_id else None
        refaccion = get_object_or_404(Refaccion, pk=refaccion_id) if refaccion_id else None

        detalle = DetalleOrden(orden=orden, servicio=servicio, refaccion=refaccion,
                               tipo_cargo=tipo_cargo, descripcion=descripcion,
                               cantidad_uni_hr=cantidad_uni_hr,
                               precio_unitario=precio_unitario, subtotal=subtotal)
        detalle.save()
        return redirect('ver_detalleorden')
    return render(request, 'detalleorden/agregar_detalleorden.html', {
        'ordenes': ordenes,
        'refacciones': refacciones,
        'servicios': servicios
    })

def ver_detalleorden(request):
    query = request.GET.get('q')
    if query:
        detalles = DetalleOrden.objects.filter(
            Q(orden__vehiculo__matricula__icontains=query) |
            Q(servicio__nombre_servicio__icontains=query) |
            Q(refaccion__nombre__icontains=query) |
            Q(tipo_cargo__icontains=query)
        ).order_by('orden__id')
    else:
        detalles = DetalleOrden.objects.all().order_by('orden__id')
    return render(request, 'detalleorden/ver_detalleorden.html', {'detalles': detalles})

def actualizar_detalleorden(request, pk):
    detalle = get_object_or_404(DetalleOrden, pk=pk)
    ordenes = Orden.objects.all().order_by('-fecha_entrada')
    refacciones = Refaccion.objects.all().order_by('nombre')
    servicios = Servicio.objects.all().order_by('nombre_servicio')
    return render(request, 'detalleorden/actualizar_detalleorden.html', {
        'detalle': detalle,
        'ordenes': ordenes,
        'refacciones': refacciones,
        'servicios': servicios
    })

def realizar_actualizacion_detalleorden(request, pk):
    if request.method == 'POST':
        detalle = get_object_or_404(DetalleOrden, pk=pk)
        orden_id = request.POST['orden']
        servicio_id = request.POST.get('servicio')
        refaccion_id = request.POST.get('refaccion')

        detalle.orden = get_object_or_404(Orden, pk=orden_id)
        detalle.servicio = get_object_or_404(Servicio, pk=servicio_id) if servicio_id else None
        detalle.refaccion = get_object_or_404(Refaccion, pk=refaccion_id) if refaccion_id else None

        detalle.tipo_cargo = request.POST['tipo_cargo']
        detalle.descripcion = request.POST['descripcion']
        detalle.cantidad_uni_hr = request.POST['cantidad_uni_hr']
        detalle.precio_unitario = request.POST['precio_unitario']
        detalle.subtotal = request.POST['subtotal']
        detalle.save()
        return redirect('ver_detalleorden')
    return redirect('ver_detalleorden')


def borrar_detalleorden(request, pk):
    detalle = get_object_or_404(DetalleOrden, pk=pk)
    if request.method == 'POST':
        detalle.delete()
        return redirect('ver_detalleorden')
    return render(request, 'detalleorden/borrar_detalleorden.html', {'detalle': detalle})
