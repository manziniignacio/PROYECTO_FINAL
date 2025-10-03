from django.contrib import admin
from .models import Mensaje

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('quien_envia', 'quien_recibe', 'contenido', 'date_time')
    search_fields = ('contenido',)
    list_filter = ('date_time', 'quien_envia', 'quien_recibe')
