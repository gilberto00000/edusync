from django.db import models

from apps.disciplinas.models import Disciplina
from core.models import BaseModel

# Create your models here.

class GradeCurricular(BaseModel):

    nome = models.CharField(max_length=255)

    ano = models.PositiveIntegerField()

    disciplinas = models.ManyToManyField(
        Disciplina, 
        related_name='grades_curriculares'
        )
    
    def __str__(self):
        return f"{self.nome} - {self.ano}"