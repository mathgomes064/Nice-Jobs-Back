from rest_framework import serializers
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer
from descriptions.serializers import DescriptionSerializer

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):

    service_owner = serializers.ReadOnlyField(source="user_id.username")
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    description = DescriptionSerializer(read_only=True)

    class Meta:
        model = Service
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
