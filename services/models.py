from django.db import models

import uuid


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_name = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    description = models.ForeignKey(
        "descriptions.Description",
        on_delete=models.CASCADE,
        null=False,
        related_name="service",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        null=False,
        related_name="service",
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=False, related_name="service"
    )

    class Meta:
        ordering = ["id"]
