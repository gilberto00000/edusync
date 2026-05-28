from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.viewsets import ModelViewSet

from .models import Professor
from .serializers import ProfessorSerializer

from apps.usuarios.permissoes import ECoordenador


@method_decorator(cache_page(60 * 5), name='list')
class ProfessorViewSet(ModelViewSet):

    permission_classes = [ECoordenador]

    serializer_class = ProfessorSerializer

    queryset = Professor.objects.filter(is_active=True)

    def get_queryset(self):

        queryset = super().get_queryset()

        nome = self.request.query_params.get("nome")

        especialidade = self.request.query_params.get(
            "especialidade"
        )

        if nome:
            queryset = queryset.filter(
                nome__icontains=nome
            )

        if especialidade:
            queryset = queryset.filter(
                especialidade__icontains=especialidade
            )

        return queryset