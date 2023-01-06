from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from services.models import Service

import ipdb


class ScheduleView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_create(self, serializer):
        service_id = self.request.data.pop("service_id")
        service_obj = get_object_or_404(Service, id=service_id)
        # ipdb.set_trace()
        serializer.save(user=self.request.user, service=service_obj)



class SchedulesDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_url_kwarg = "pk"
