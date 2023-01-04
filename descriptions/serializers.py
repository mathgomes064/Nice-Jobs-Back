from rest_framework import serializers

from .models import Description


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = [
            "id",
            "serviceDescription",
            "serviceValue",
            "atuationArea",
        ]
