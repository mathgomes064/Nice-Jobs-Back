from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class ScheduleView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class SchedulesDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_url_kwarg = "pk"
