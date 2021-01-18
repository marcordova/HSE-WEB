from rest_framework import serializers
from hotel.models import Type
from hotel.models import Room

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
         model = Type
         fields = ['id','name']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
         model = Room
         fields = ['id','number', 'description', 'type']