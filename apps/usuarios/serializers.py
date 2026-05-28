from rest_framework import serializers

from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario

        fields = [
            "id",
            "username",
            "email",
            "perfil",
        ]


class UsuarioCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario

        fields = [
            "id",
            "username",
            "email",
            "password",
            "perfil",
        ]

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):

        user = Usuario.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            perfil=validated_data["perfil"],
        )

        return user