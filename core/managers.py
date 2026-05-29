from django.db import models


class AtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class TodosManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
