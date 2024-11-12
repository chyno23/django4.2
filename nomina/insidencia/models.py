from django.db import models
from decimal import Decimal

class Insidencia(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    ]
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"La incidencia es : {self.titulo} - Estado: {self.estado}"

 



class Banco(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='bancos_imagenes/', blank=True, null=True)
    status1 = models.BooleanField(default=True)
    status2 = models.BooleanField(default=False)
    custom1 = models.CharField(max_length=255, blank=True, null=True)
    custom2 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    total_ventas = models.DecimalField(max_digits=10, decimal_places=2)
    total_ganancias = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_ganancias1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Campo para almacenar

    @property
    def porcentaje_ganancias(self):
        # Evitamos división por cero
        if self.total_ventas == 0:
            return 0
        # Calculamos el porcentaje de ganancias
        return ((self.total_ganancias / self.total_ventas) * 100).quantize(Decimal('0.01'))

    def save(self, *args, **kwargs):
        # Calculamos el porcentaje antes de guardar
        self.porcentaje_ganancias1 = self.porcentaje_ganancias
        super().save(*args, **kwargs)  # Guardamos en la base de datos

