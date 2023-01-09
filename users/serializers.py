from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

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
        }
        depth = 1
