from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Individual(models.Model):
    first_name = models.CharField(max_length=63, null=False, blank=False)
    last_name = models.CharField(max_length=63, null=False, blank=False)
    national_id = models.CharField(max_length=10, validators=[MinLengthValidator(10)], null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.national_id})"
