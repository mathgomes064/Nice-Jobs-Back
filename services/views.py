from django.shortcuts import get_object_or_404
from users.models import User
from .models import Service
from .serializers import ServiceSerializer, ListServiceByUserIdSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerService

from .pagination import CustomServiceResultsSetPagination


class ServiceView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    pagination_class = CustomServiceResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerService]

    lookup_url_kwarg = "service_id"


class ListServiceByUserId(generics.ListAPIView):
    serializer_class = ListServiceByUserIdSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user_obj = get_object_or_404(User, pk=user_id)

        return Service.objects.filter(user=user_obj)
