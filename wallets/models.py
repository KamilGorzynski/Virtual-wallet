from django.db import models
from django.utils.timezone import now


class CompanyData(models.Model):
    nip = models.BigIntegerField(blank=True, null=True)
    regon = models.BigIntegerField(blank=True, null=True)
    company_start_date = models.DateTimeField(default=now())

    def __str__(self):
        return str(self.nip)


class Wallet(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=28, default='0'*26)
    country = models.CharField(max_length=28, default='Poland')
    ballance = models.DecimalField(max_digits=19, decimal_places=2)
    creation_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    is_company = models.BooleanField(default=False)
    company_data = models.OneToOneField(CompanyData, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + '- Wallet'
