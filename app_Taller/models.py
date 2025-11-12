from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()
    rfc = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='clientes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: VEHICULO
# ==========================================
class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    anio = models.IntegerField()
    kilometraje = models.IntegerField()
    imagen = models.ImageField(upload_to='vehiculos/', blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"

# ==========================================
# MODELO: PERSONAL
# ==========================================
class Personal(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    fecha_contratacion = models.DateField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    telefono_contacto = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='personal/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cargo})"


# ==========================================
# MODELO: PROVEEDOR
# ==========================================
class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    contacto_nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    rfc_fiscal = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_empresa

# ==========================================
# MODELO: REFACCION
# ==========================================
class Refaccion(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    stock = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: SERVICIO
# ==========================================
class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_estimado_horas = models.DecimalField(max_digits=5, decimal_places=2)
    aplica_garantia = models.BooleanField()

    def __str__(self):
        return self.nombre_servicio

# ==========================================
# MODELO: ORDEN
# ==========================================
class Orden(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    personal_recepcion = models.ForeignKey(Personal, related_name='ordenes_recepcionadas', on_delete=models.SET_NULL, null=True)
    personal_mecanico = models.ForeignKey(Personal, related_name='ordenes_trabajadas', on_delete=models.SET_NULL, null=True)
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida_estimada = models.DateTimeField()
    fecha_salida = models.DateTimeField(null=True, blank=True)
    problema = models.TextField()
    testigos_encendidos = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=255)

    def __str__(self):
        return f"Orden #{self.pk} - {self.vehiculo}"


# ==========================================
# MODELO: DETALLEORDEN
# ==========================================
class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True, blank=True)
    refaccion = models.ForeignKey(Refaccion, on_delete=models.CASCADE, null=True, blank=True)
    tipo_cargo = models.CharField(max_length=255) # 'servicio' o 'refaccion'
    descripcion = models.TextField()
    cantidad_uni_hr = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de Orden #{self.orden.pk} - {self.tipo_cargo}"