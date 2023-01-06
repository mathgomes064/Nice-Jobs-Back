from rest_framework import serializers
from .models import Schedule
from users.serializers import UserSerializer
from services.serializers import ServiceSerializer


class ScheduleSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    class Meta:
        model = Schedule
        fields = "__all__"

    def create(self, validated_data):
        return Schedule.objects.create(**validated_data)
