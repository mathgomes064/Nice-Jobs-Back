from .models import Service
from .serializers import ServiceSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from descriptions.models import Description
from categories.models import Category
from users.permissions import IsOwnerResource

from .pagination import CustomServiceResultsSetPagination


class ServiceView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = CustomServiceResultsSetPagination

    def perform_create(self, serializer):
        category_id = self.request.data.pop("category")
        description_dict = self.request.data.pop("description")

        category_obj = Category.objects.get_or_create(id=category_id)[0]

        description_obj = Description.objects.create(**description_dict)

        serializer.save(
            user=self.request.user, description=description_obj, category=category_obj
        )


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerResource]
