from django.contrib import admin

from .models import Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nome",
        "disciplina",
        "professor",
        "ano_letivo",
    )

    search_fields = (
        "nome",
        "disciplina__nome",
        "professor__nome",
    )

    list_filter = (
        "ano_letivo",
        "disciplina",
    )