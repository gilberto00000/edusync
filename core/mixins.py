from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response


class SoftDeleteModelMixin:
    def destroy(self, request, *args, **kwargs):

        instance = self.get_object()

        instance.soft_delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class CacheListMixin:
    cache_timeout = 60 * 5

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)
