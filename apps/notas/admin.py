from django.contrib import admin

from .models import Notas


@admin.register(Notas)
class NotaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "aluno",
        "avaliacao",
        "nota",
    )

    search_fields = (
        "aluno__nome",
        "avaliacao__titulo",
    )

    list_filter = (
        "avaliacao",
    )