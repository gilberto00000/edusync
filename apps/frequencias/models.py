from django.db import models
# Create your models here.
from apps.alunos.models import Aluno
from apps.professores.models import Professor
from apps.turmas.models import Turma
from  core.models import BaseModel

class Frequencia(BaseModel):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='frequencias'
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='frequencias'
    )

    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='frequencias'
    )

    data = models.DateField()

    presente = models.BooleanField(default=False)

    observacao = models.TextField(
        max_length=1000, 
        blank=True, 
        null=True
    )
    
    class Meta:
        unique_together = ('aluno', 'turma', 'data')

    def __str__(self):
        status = "Presente" if self.presente else "Ausente"
        
        return f"{self.aluno.nome} - {self.turma.nome} - {self.data}: {status}"
