from django.db import models

# Create your models here.
class Autores(models.Model):
    Nombre = models.CharField(max_length=200)
    Edad = models.IntegerField()
    Nacionalidad = models.CharField(max_length=100)
    FechaDeNacimiento = models.DateField()

    def __str__(self):
        return self.Nombre

class Canciones(models.Model):
    Titulo = models.CharField(max_length=200)
    Autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
    FechaLanzamiento = models.DateField()

    def __str__(self):
        return self.Titulo

        