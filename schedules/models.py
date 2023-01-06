from django.db import models
import uuid


class Schedule(models.Model):
    class Meta:
        ordering = ("id",)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    hour = models.TimeField()
    is_done = models.BooleanField(
        default=False,
    )

    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="schedule_user",
    )
