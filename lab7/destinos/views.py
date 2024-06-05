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

def modificar_destino(request, id):
    destino = get_object_or_404(Destino, id=id)
    if request.method == 'POST':
        form = DestinoForm(request.POST, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'destinos/form_destino.html', {'form': form})

def eliminar_destino(request, id):
    destino = get_object_or_404(Destino, id=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('listar_destinos')
    return render(request, 'destinos/eliminar_destino.html', {'destino': destino})
