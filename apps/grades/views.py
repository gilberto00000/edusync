from rest_framework.viewsets import ModelViewSet

from .models import GradeCurricular
from .serializers import GradeCurricularSerializer

from apps.usuarios.permissoes import ECoordenador


class GradeCurricularViewSet(ModelViewSet):

    permission_classes = [ECoordenador]

    serializer_class = GradeCurricularSerializer

    queryset = GradeCurricular.objects.filter(
        is_active=True
    )