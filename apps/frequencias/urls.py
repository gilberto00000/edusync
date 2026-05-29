from rest_framework.routers import DefaultRouter

from .views import FrequenciaViewSet

router = DefaultRouter()

router.register(
    r'frequencias',
    FrequenciaViewSet,
    basename='frequencias'
)

urlpatterns = router.urls