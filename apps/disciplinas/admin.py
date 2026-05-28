from django.contrib import admin

from .models import Disciplina


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nome",
        "carga_horaria",
    )

    search_fields = (
        "nome",
    )

    list_filter = (
        "carga_horaria",
    )