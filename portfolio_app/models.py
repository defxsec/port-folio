from django.db import models

# Create your models here.
class Producto(models.Model):
    codigoBarras = models.CharField(max_length=100, default=0)
    title = models.CharField(max_length=200)
    stock = models.PositiveBigIntegerField(default=0)
    precio = models.PositiveBigIntegerField(default=0)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField(auto_now=True)

    # Para que muestre en el panel de administracion con el titulo
    # en vez de Object
    def __str__(self):
        return self.title