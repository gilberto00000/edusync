from rest_framework.viewsets import ModelViewSet

from .models import Frequencia
from .serializers import FrequenciaSerializer
from apps.usuarios.permissoes import (
    ECoordenadorOuProfessor
)


class FrequenciaViewSet(ModelViewSet):

    permission_classes = [
            ECoordenadorOuProfessor
        ]

    serializer_class = FrequenciaSerializer

    queryset = Frequencia.objects.filter(
        is_active=True
    )

    def get_queryset(self):

        queryset = super().get_queryset()

        aluno = self.request.query_params.get(
            "aluno"
        )

        turma = self.request.query_params.get(
            "turma"
        )

        data = self.request.query_params.get(
            "data"
        )

        if aluno:
            queryset = queryset.filter(
                aluno_id=aluno
            )

        if turma:
            queryset = queryset.filter(
                turma_id=turma
            )

        if data:
            queryset = queryset.filter(
                data=data
            )

        return queryset