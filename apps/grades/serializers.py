from rest_framework import serializers

from .models import GradeCurricular


class GradeCurricularSerializer(serializers.ModelSerializer):

    class Meta:
        model = GradeCurricular

        fields = "__all__"