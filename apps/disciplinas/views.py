from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.viewsets import ModelViewSet

from .models import Disciplina
from .serializers import DisciplinaSerializer
from apps.usuarios.permissoes import ECoordenador

@method_decorator(cache_page(60 * 5), name='list')
class DisciplinaViewSet(ModelViewSet):

    permission_classes = [ECoordenador]

    serializer_class = DisciplinaSerializer

    queryset = Disciplina.objects.filter(is_active=True)

    def get_queryset(self):

        queryset = super().get_queryset()

        nome = self.request.query_params.get("nome")

        if nome:
            queryset = queryset.filter(
                nome__icontains=nome
            )

        return queryset