from rest_framework import serializers

from .models import Notas


class NotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notas

        fields = "__all__"