from django.contrib import admin

from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nome",
        "matricula",
        "email",
        "is_active",
    )

    search_fields = (
        "nome",
        "matricula",
        "email",
    )

    list_filter = (
        "is_active",
    )