from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "date",
            "hour",
            "is_done",
            # "service",
            # "user",
        ]

    def create(self, validated_data: dict) -> Schedule:
        return Schedule.objects.create_superuser(**validated_data)
