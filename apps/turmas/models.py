from django.db import models

from apps.alunos.models import Aluno
from apps.disciplinas.models import Disciplina
from core.models import BaseModel
from apps.professores.models import Professor

# Create your models here.

class Turma(BaseModel):

    nome = models.CharField(max_length=255)

    ano_letivo = models.PositiveIntegerField()

    professor = models.ForeignKey(
        Professor,
        on_delete=models.PROTECT,
        related_name='turmas'
    )

    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.PROTECT,
        related_name='turmas'
    )

    alunos = models.ManyToManyField(
        Aluno,
        related_name='turmas'
    )
    
    def __str__(self):
        return f"{self.nome} - {self.disciplina.nome}"