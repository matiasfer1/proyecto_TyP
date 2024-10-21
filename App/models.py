from django.db import models

# Create your models here.
class Nombre(models.Model):
        nombre = models.CharField(max_length=255)
        fecha = models.DateField(auto_now_add=True)
        
        def __str__(self):
            return self.nombre
        

class Sorteo(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre