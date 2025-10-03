from django.urls import path
from . import views

urlpatterns = [
    path('mensajes/', views.lista_mensajes, name='lista_mensajes'),
]
