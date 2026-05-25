from django.db import models
from core.models import BaseModel

# Create your models here.

class Disciplina(BaseModel):

    nome = models.CharField(max_length=255)

    codigo = models.CharField(
        max_length=50, 
        unique=True
    )

    carga_horaria = models.PositiveIntegerField()

    descricao = models.TextField(
        max_length=1000, 
        blank=True, 
        null=True
        )

    def __str__(self):
        return self.nome