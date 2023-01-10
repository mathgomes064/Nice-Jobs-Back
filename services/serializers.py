from rest_framework import serializers
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer
from descriptions.serializers import DescriptionSerializer

from categories.models import Category
from descriptions.models import Description
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):

    service_owner = serializers.ReadOnlyField(source="user_id.username")
    user = UserSerializer(read_only=True)
    category = CategorySerializer()
    description = DescriptionSerializer()

    def create(self, validated_data):
        category_dict = validated_data.pop("category")
        description_dict = validated_data.pop("description")

        category_obj = Category.objects.get_or_create(**category_dict)[0]
        description_obj = Description.objects.create(**description_dict)

        return Service.objects.create(
            **validated_data, category=category_obj, description=description_obj
        )

    class Meta:
        model = Service
        fields = [
            "id",
            "service_name",
            "service_owner",
            "is_active",
            "created_at",
            "updated_at",
            "description",
            "user",
            "category",
        ]
        read_only_fields = ["created_at", "updated_at"]


class ListServiceByUserIdSerializer(serializers.ModelSerializer):
    service_owner = serializers.ReadOnlyField(source="user_id.username")
    category = CategorySerializer()
    description = DescriptionSerializer()

    class Meta:
        model = Service
        fields = [
            "id",
            "service_name",
            "service_owner",
            "is_active",
            "created_at",
            "updated_at",
            "description",
            "category",
        ]
