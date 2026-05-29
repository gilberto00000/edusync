from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.viewsets import ModelViewSet

from .models import Turma
from .serializers import TurmaSerializer

from apps.usuarios.permissoes import ECoordenador


@method_decorator(cache_page(60 * 5), name='list')
class TurmaViewSet(ModelViewSet):

    permission_classes = [ECoordenador]

    serializer_class = TurmaSerializer

    queryset = Turma.objects.filter(
        is_active=True
    )

    def get_queryset(self):

        queryset = super().get_queryset()

        disciplina = self.request.query_params.get(
            "disciplina"
        )

        professor = self.request.query_params.get(
            "professor"
        )

        ano_letivo = self.request.query_params.get(
            "ano_letivo"
        )

        if disciplina:
            queryset = queryset.filter(
                disciplina_id=disciplina
            )

        if professor:
            queryset = queryset.filter(
                professor_id=professor
            )

        if ano_letivo:
            queryset = queryset.filter(
                ano_letivo=ano_letivo
            )

        return queryset