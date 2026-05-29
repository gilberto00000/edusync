from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    list_display = (
        "id",
        "username",
        "email",
        "perfil",
        "is_staff",
    )

    search_fields = (
        "username",
        "email",
    )

    list_filter = (
        "perfil",
        "is_staff",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Informações do Sistema",
            {
                "fields": ("perfil",),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Informações do Sistema",
            {
                "fields": ("perfil",),
            },
        ),
    )