from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):

    service_owner = serializers.ReadOnlyField(source='user_id.username')

    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
