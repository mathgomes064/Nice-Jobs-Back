from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Schedule
from users.serializers import UserSerializer
from services.serializers import ServiceSerializer
from services.models import Service


class ScheduleSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    service_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Schedule
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Schedule.objects.all(),
                fields=["date", "hour", "service_id"],
            )
        ]

    def create(self, validated_data):
        service_id = validated_data.pop("service_id")
        service_obj = get_object_or_404(Service, id=service_id)
        return Schedule.objects.create(**validated_data, service=service_obj)
