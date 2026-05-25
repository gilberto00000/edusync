from django.db import models

from apps.turmas.models import Turma
from core.models import BaseModel

# Create your models here.

class Avaliacao(BaseModel):

    titulo = models.CharField(max_length=255)

    descricao = models.TextField(
        max_length=1000, 
        blank=True, 
        null=True
        )
    
    peso = models.DecimalField(
        max_digits=5, 
        decimal_places=2
        )

    data_avaliacao = models.DateField()

    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='avaliacoes'
    )      

    def __str__(self):
        return f"{self.titulo} - {self.turma.nome}"