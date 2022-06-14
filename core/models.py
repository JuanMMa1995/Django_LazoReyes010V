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

opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class contacto(models.Model):
    nombreP = models.CharField(max_length=50)
    correoP = models.EmailField()
    tipo_Consulta = models.IntegerField()
    mensaje = models.TextField()
    aviso = models.BooleanField()

    def __str__(self):
        return self.nombre