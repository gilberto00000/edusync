from django.contrib import admin

from .models import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nome",
        "especialidade",
        "email",
    )

    search_fields = (
        "nome",
        "especialidade",
        "email",
    )

    list_filter = (
        "especialidade",
    )