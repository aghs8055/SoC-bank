import random
import string
import time

from django.db.models import F, Q

from individuals.models import Individual
from accounts.models import Account


def random_string(length):
    return "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=length))


def random_national_id():
    return "".join(random.choices(string.digits, k=10))


def create_random_accounts(cnt=20000):
    individuals = random.choices(
        Individual.objects.bulk_create(
            [
                Individual(first_name=random_string(7), last_name=random_string(7), national_id=random_national_id())
                for _ in range(cnt)
            ]
        ),
        k=cnt,
    )
    accounts = Account.objects.bulk_create(
        [Account(owner=individuals[i], balance=random.randint(0, 10000000000)) for i in range(cnt)]
    )


def accounts_with_owner_name_and_balance():
    return Account.objects.select_related("owner").values("owner__first_name", "owner_last_name", "balance")


def account_with_max_balance():
    return Account.objects.order_by("-balance")[0]


def five_accounts_with_min_balance():
    return Account.objects.order_by("balance")[:5]


def transfer_balance(from_account_id, to_account_id, amount):
    try:
        from_account = Account.objects.get(id=from_account_id)
        to_account = Account.objects.get(id=to_account_id)
        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount
            from_account.save()
            to_account.save()
            return True
    except Account.DoesNotExist:
        pass
    return False


def accounts_with_id_greater_than_balance():
    return Account.objects.filter(id__gt=F("balance"))


def accounts_with_national_id_greater_than_balance():
    return Account.objects.filter(owner__national_id__gt=F("balance"))


def accounts_with_balance_greater_than_2000000_or_less_than_1000000():
    start_time = time.time()
    result = Account.objects.filter(Q(balance__gt=2000000) | Q(balance__lt=1000000))
    print(f"Time: {time.time() - start_time}")
    return result
