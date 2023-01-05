from .models import Schedule
from .serializers import ScheduleSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class ScheduleView(generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = ["user_id"]

    # def get_queryset(self):
    #     schedule_id = self.kwargs.get("schedule_id")
    #     schedule_obj = get_object_or_404(Schedule, pk=schedule_id)
    #     schedule = Schedule.objects.filter(service_id=schedule_obj)

    #     return schedule

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# class SchedulesDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Schedule.objects.all()
#     serializer_class = ScheduleSerializer
# authentication_classes = [JWTAuthentication]
# permission_classes = [IsAuthenticated]
