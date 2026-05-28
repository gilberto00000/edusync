from rest_framework.viewsets import ModelViewSet

from .models import Avaliacao
from .serializers import AvaliacaoSerializer
from apps.usuarios.permissoes import (
    ECoordenadorOuProfessor
)


class AvaliacaoViewSet(ModelViewSet):

    permission_classes = [
        ECoordenadorOuProfessor
    ] 

    serializer_class = AvaliacaoSerializer

    queryset = Avaliacao.objects.filter(
        is_active=True
    )

    def get_queryset(self):

        queryset = super().get_queryset()

        turma = self.request.query_params.get(
            "turma"
        )

        if turma:
            queryset = queryset.filter(
                turma_id=turma
            )

        return queryset