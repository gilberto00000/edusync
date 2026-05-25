from django.db import models

from apps.avaliacoes.models import Avaliacao
from core.models import BaseModel
from apps.alunos.models import Aluno
# Create your models here.

class Notas(BaseModel):

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='notas'
    )

    avaliacao = models.ForeignKey(
        Avaliacao,
        on_delete=models.CASCADE,
        related_name='notas'
    )

    nota = models.DecimalField(
        max_digits=5, 
        decimal_places=2
        )

    class Meta:
        unique_together = ('aluno', 'avaliacao')

    def __str__(self):
        return f"{self.aluno.nome} - {self.avaliacao}: {self.nota}"


