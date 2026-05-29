from rest_framework.routers import DefaultRouter

from .views import TurmaViewSet

router = DefaultRouter()

router.register(
    r'turmas',
    TurmaViewSet,
    basename='turmas'
)

urlpatterns = router.urls