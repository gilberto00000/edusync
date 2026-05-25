from django.db import models

from apps.usuarios.models import Usuario
from core.models import BaseModel

# Create your models here.

class Professor(BaseModel):

    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='professor'
    )

    nome = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    especialidade = models.CharField(max_length=255)


    def __str__(self):
        return self.nome