from rest_framework.generics import (
    ListCreateAPIView,
)
from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleView(ListCreateAPIView):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
