from rest_framework import serializers
from .models import User
from services.serializers import ServiceSerializer


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    def get_services(self):
        services = ServiceSerializer(many=True)
        return services

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "fone",
            "email",
            "bio",
            "password",
            "is_premium",
            "is_offering",
            "is_active",
            "created_at",
            "updated_at",
            "services",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "services": {"read_only": True},
        }
