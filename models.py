from django.db import models
from django.utils import timezone


class TipodeTrabajo(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Turnos(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Empleados (models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    DNI = models.IntegerField()
    direccion_de_correo = models.CharField(max_length=200)
    fecha_de_nacimiento = models.DateTimeField(default=timezone.now)
    numero_de_empleado = models.IntegerField()
    telefono = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=200)
    tipo_de_trabajo = models.ForeignKey('TipodeTrabajo')
    turnos = models.ForeignKey('Turnos')

    def __str__(self):
        return self.apellido

class Clientes (models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    numero_de_cliente = models.IntegerField()
    telefono = models.IntegerField()
    direccion_de_correo = models.CharField(max_length=200)

    def __str__(self):
        return self.apellido

class Plataformas (models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Productos (models.Model):
    nombre_del_producto = models.CharField(max_length=200)
    id_del_producto = models.IntegerField()
    plataforma = models.ManyToManyField(Plataformas)
    precio = models.CharField(max_length=200)
    stock = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_del_producto

class Proveedor (models.Model):
    nombre_del_proveedor = models.CharField(max_length=200)
    apellido_del_proveedor = models.CharField(max_length=200)
    telefono = models.IntegerField()
    direccion_de_correo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_del_proveedor


