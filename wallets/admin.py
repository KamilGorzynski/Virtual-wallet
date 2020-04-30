from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Wallet)
class WalletAdmin (admin.ModelAdmin):
    list_display = ('user', 'ballance', 'creation_date', 'active')


@admin.register(CompanyData)
class WalletAdmin (admin.ModelAdmin):
    pass
