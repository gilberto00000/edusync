from django.contrib import admin

from .models import Frequencia


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "aluno",
        "turma",
        "professor",
        "data",
        "presente",
    )

    search_fields = (
        "aluno__nome",
        "turma__nome",
    )

    list_filter = (
        "presente",
        "data",
    )