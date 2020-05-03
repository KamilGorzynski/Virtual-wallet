from django.db import models
from django.utils.timezone import now

from Wallet.fin import CURRENCY_TYPES


class Transfer(models.Model):
    source_account = models.CharField(max_length=28, default='0'*26)
    beneficiary_account = models.CharField(max_length=28, default='0'*26)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_TYPES)
    title = models.CharField(max_length=70, blank=True, null=True)
    transfer_date = models.DateTimeField(default=now())
