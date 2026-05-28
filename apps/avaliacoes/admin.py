from django.contrib import admin

from .models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "titulo",
        "turma",
        "peso",
        "data_avaliacao",
    )

    search_fields = (
        "titulo",
    )

    list_filter = (
        "data_avaliacao",
        "turma",
    )