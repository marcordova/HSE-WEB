from django.db import models
from datetime import date

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Tipo de habitación')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='Tipo'
        verbose_name_plural='Tipos'

    def __str__(self): 
        return self.name

class Room(models.Model):
    number = models.IntegerField(verbose_name = 'Número de habitación',unique = True)
    description = models.TextField(verbose_name = 'Descripción')
    image = models.ImageField("Imagen", upload_to='hotel', blank=True)
    price = models.IntegerField(verbose_name = 'Precio') 
    created_on=models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='Habitación'
        verbose_name_plural='Habitaciones'

    def __str__(self): 
        return 'R:{} -> T:{}'.format(self.number, self.type.name)