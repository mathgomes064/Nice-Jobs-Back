from django.db import models

import uuid


class Category(models.Model):

    CONSTRUCAO = "Construção civil"
    MANUTENCAO = "Manutenção de Eletrônicos"
    FRETE = "Frete"
    DOMESTICOS = "Serviços Domésticos"
    OUTROS = "Outros"

    CATEGORY_CHOICES = (
        (CONSTRUCAO, "Construção civil"),
        (MANUTENCAO, "Manutenção de Eletrônicos"),
        (FRETE, "Frete"),
        (DOMESTICOS, "Serviços Domésticos"),
        (OUTROS, "Outros"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=OUTROS)

    class Meta:
        ordering = ["id"]
