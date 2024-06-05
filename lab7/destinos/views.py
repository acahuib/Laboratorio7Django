from django.shortcuts import render, redirect, get_object_or_404
from .models import Destino
from .forms import DestinoForm

def listar_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'destinos/listar_destinos.html', {'destinos': destinos})

