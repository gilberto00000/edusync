from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    
    PERFIL_CHOICES = (
        ('COORDENADOR', 'Coordenador'),
        ('PROFESSOR', 'Professor'),
        ('ALUNO', 'Aluno'),
    )

    perfil = models.CharField(
        max_length=20,
        choices=PERFIL_CHOICES,
    )

    def __str__(self):
        return self.username