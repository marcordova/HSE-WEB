from django.contrib import admin
from hotel.models import Type
from hotel.models import Room
from hotel.models import Client
from hotel.models import Pay
from hotel.models import Reservation

# Register your models here.
admin.site.register(Type)
admin.site.register(Room)
admin.site.register(Client)
admin.site.register(Pay)
admin.site.register(Reservation)
