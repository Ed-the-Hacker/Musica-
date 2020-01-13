from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect

from .models import Autores, Canciones
# Create your views here.
def canciones_list(request):
    listaCanciones = Canciones.objects.order_by('FechaLanzamiento')
    return render(request, 'canciones/canciones_list.html', {'canciones': listaCanciones})