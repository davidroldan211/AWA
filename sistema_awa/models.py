from django.db import models

# Create your models here.
class variables(models.Model):
    ph=models.CharField(max_length=10)
    temperatura=models.CharField(max_length=10)
    humedad=models.CharField(max_length=10)
    fecha=models.DateTimeField()

class awa(models.Model):
    Fecha_y_hora=models.DateTimeField()
    Temperatura=models.CharField(max_length=10)
    Humedad=models.CharField(max_length=10)
    OD=models.CharField(max_length=10)
