from django.db import models

from apps.usuarios.models import Usuario
from core.models import BaseModel

# Create your models here.

class Aluno(BaseModel):

    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='aluno'
    )

    nome = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    matricula = models.CharField(
        max_length=50, 
        unique=True
    )

    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome