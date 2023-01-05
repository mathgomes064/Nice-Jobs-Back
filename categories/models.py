from django.db import models


class Category(models.Model):
    service_description = models.CharField(max_length=200, null=False)
    service_value = models.DecimalField(
        max_digits=5, decimal_places=2, null=False)
    atuation_area = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['id']
