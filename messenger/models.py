from django.db import models
from django.contrib.auth.models import User 

class Mensaje(models.Model):
    quien_envia = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensaje_enviado")
    quien_recibe = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensaje_recibido")
    contenido = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"De {self.quien_envia} a {self.quien_recibe}: {self.contenido[:20]}"