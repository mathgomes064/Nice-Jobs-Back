from django.db import models


class Service(models.Model):

    service_name = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    description_id = models.ForeignKey(
        "descriptions.Description", on_delete=models.CASCADE, null=False, related_name="service_description")
    category_id = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, null=False, related_name="service_category")
    user_id = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=False, related_name="service_user")

    class Meta:
        ordering = ['id']
