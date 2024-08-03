from django.db import models

from individuals.models import Individual


class Account(models.Model):
    owner = models.ForeignKey(Individual, on_delete=models.CASCADE, null=False)
    balance = models.PositiveIntegerField(default=0, null=False)
