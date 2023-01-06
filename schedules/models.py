from django.db import models


class Schedule(models.Model):
    class Meta:
        ordering = ("id",)

    date = models.DateField()
    hour = models.TimeField()
    is_done = models.BooleanField(
        default=False,
    )

    service_id = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="schedule_user",
    )
