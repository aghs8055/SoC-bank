from django.db.models.aggregates import Sum

from individuals.models import Individual


def individuals_balance():
    return Individual.objects.annotate(balance=Sum("account__balance")).values(
        "first_name", "last_name", "national_id", "balance"
    )
