from rest_framework.routers import DefaultRouter

from .views import GradeCurricularViewSet

router = DefaultRouter()

router.register(
    r'grades',
    GradeCurricularViewSet,
    basename='grades'
)

urlpatterns = router.urls