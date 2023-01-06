from django.db import models
import uuid


class Description(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_description = models.CharField(max_length=50)
    service_value = models.DecimalField(max_digits=5, decimal_places=2)
    atuation_area = models.CharField(max_length=50)
