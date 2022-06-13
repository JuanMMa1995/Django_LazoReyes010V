from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True, verbose_name='nombre')
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fec_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="producto", null=True)
    def __str__(self):
        return self.nombre
