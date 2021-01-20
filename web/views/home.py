from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from hotel.models import Room

class HomeView(View):
    '''
    Vista de la pagina Home
    '''
    template_name = 'home.html'

    def get(self, request):
        habitaciones = Room.objects.all()
        perrito = 'gatito'
        datos = {
          'name' : 'Arturo',
          'frutas': ['manzana', 'pera', 'tomate'],
          'habitaciones': habitaciones,
        }
        return render(request, self.template_name, datos)
