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

class Client(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Nombre')
    lastname = models.CharField(max_length = 100, verbose_name = 'Apellido')
    document = models.CharField(max_length = 100, verbose_name = 'Número de documento de identidad')
    email = models.CharField(max_length = 100, verbose_name = 'Correo electrónico')
    password = models.CharField( max_length = 100, verbose_name = 'Contrasenia')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def __str__(self): 
        return self.name + self.lastname
        
class Pay(models.Model):
    amount = models.IntegerField(verbose_name = 'Monto a pagar')
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='Pago'
        verbose_name_plural='Pagos'

    def __str__(self): 
        return 'C:{} -> P:{}'.format(self.client.document, self.amount)
        
class Reservation(models.Model):
    checkin = models.DateTimeField(verbose_name='Fecha de llegada')
    night = models.IntegerField(verbose_name = '¿Cuántas noches?') 
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    pay = models.ForeignKey('Pay', on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['created_on']
        verbose_name='Reserva'
        verbose_name_plural='Reservaciones'

    def __str__(self): 
        return 'R:{} -> C:{} -> P:{}'.format(self.checkin, self.client.document, self.pay.amount)