from rest_framework.routers import DefaultRouter

from .views import DisciplinaViewSet

router = DefaultRouter()

router.register(
    r'disciplinas',
    DisciplinaViewSet,
    basename='disciplinas'
)

urlpatterns = router.urls