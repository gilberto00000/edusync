from django.contrib import admin

from .models import GradeCurricular


@admin.register(GradeCurricular)
class GradeAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nome",
        "ano",
    )

    search_fields = (
        "nome",
    )

    list_filter = (
        "ano",
    )