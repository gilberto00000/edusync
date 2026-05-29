import email

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.viewsets import ModelViewSet
from apps.usuarios.permissoes import ECoordenador


from .models import Aluno
from .serializers import AlunoSerializer


@method_decorator(cache_page(60 * 5), name='list')
class AlunoViewSet(ModelViewSet):

    permission_classes = [ECoordenador]

    serializer_class = AlunoSerializer

    queryset = Aluno.objects.filter(is_active=True)

    def get_queryset(self):

        queryset = super().get_queryset()

        nome = self.request.query_params.get("nome")

        matricula = self.request.query_params.get("matricula")

        email = self.request.query_params.get("email")

        if nome:
            queryset = queryset.filter(
                nome__icontains=nome
            )

        if matricula:
            queryset = queryset.filter(
                matricula__icontains=matricula
            )

        if email:
            queryset = queryset.filter(
                email__icontains=email
            )

        return queryset