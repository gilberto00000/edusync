from rest_framework.routers import DefaultRouter

from .views import ProfessorViewSet

router = DefaultRouter()

router.register(
    r'professores',
    ProfessorViewSet,
    basename='professores'
)

urlpatterns = router.urls