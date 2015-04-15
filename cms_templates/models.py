from django.db import models

# Create your models here.

class PutApp(models.Model):
    titulo = models.CharField(max_length=32)
    contenido = models.TextField()
