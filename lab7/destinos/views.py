from django.shortcuts import render, redirect, get_object_or_404
from .models import Destino
from .forms import DestinoForm

def listar_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'destinos/listar_destinos.html', {'destinos': destinos})

def anadir_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
    else:
        form = DestinoForm()
    return render(request, 'destinos/form_destino.html', {'form': form})

