from django import forms
from .models import Destino

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ['nombre', 'descripcion', 'ubicacion', 'fecha_visita']

