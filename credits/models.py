from django.db import models

from Wallet.fin import CREDIT_TYPES


class Credit(models.Model):
    amount = models.IntegerField(default=0)
    type = models.CharField(choices=CREDIT_TYPES, max_length=27)
    credit_ballance = models.IntegerField(default=0)
    rates = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)


class Offer(models.Model):
    title = models.CharField(max_length=27)
    text = models.TextField()


class OfferComment(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    comment = models.TextField(default='')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
