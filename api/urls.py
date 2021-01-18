from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'type', views.TypeViewSet)
router.register(r'room', views.RoomViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
   
    
]