from django.db import models


class Schedule(models.Model):
    class Meta:
        ordering = ("id",)

    date = models.DateField()
    hour = models.TimeField()
    is_done = models.BooleanField(
        default=False,
    )

    # service = models.ForeignKey(
    #     "services.Service",
    #     on_delete=models.CASCADE,
    #     related_name="schedules",
    # )

    # user = models.ForeignKey(
    #     "users.User",
    #     on_delete=models.CASCADE,
    #     related_name="schedules",
    # )
