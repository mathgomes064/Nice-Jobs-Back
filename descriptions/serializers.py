from rest_framework import serializers

from .models import Description


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = [
            "id",
            "service_description",
            "service_value",
            "atuation_area",
        ]
