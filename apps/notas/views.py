from rest_framework.viewsets import ModelViewSet

from .models import Notas
from .serializers import NotaSerializer
from apps.usuarios.permissoes import NotaPermissao

class NotaViewSet(ModelViewSet):

    permission_classes = [NotaPermissao]

    serializer_class = NotaSerializer

    queryset = Notas.objects.filter(is_active=True)

    def get_queryset(self):

        queryset = super().get_queryset()

        aluno = self.request.query_params.get(
            "aluno"
        )

        avaliacao = self.request.query_params.get(
            "avaliacao"
        )

        if aluno:
            queryset = queryset.filter(
                aluno_id=aluno
            )

        if avaliacao:
            queryset = queryset.filter(
                avaliacao_id=avaliacao
            )

        return queryset