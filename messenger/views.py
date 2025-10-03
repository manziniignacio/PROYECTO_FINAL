from django.shortcuts import render
from .models import Mensaje

def lista_mensajes(request):
    mensajes = Mensaje.objects.all().order_by('-date_time')  # mensajes más nuevos primero
    return render(request, 'messenger/mensajes_list.html', {'mensajes': mensajes})
