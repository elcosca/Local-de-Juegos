from django.shortcuts import render
from .models import Clientes

def vistaclientes(request):
        clientes = Clientes.objects.all()
        return render(request, 'localdejuego/clientes.html', {'clientes': clientes})