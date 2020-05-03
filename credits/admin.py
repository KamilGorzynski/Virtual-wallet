from django.contrib import admin

from .models import Credit, Offer, OfferComment
# Register your models here.


@admin.register(Credit)
class CreditAdmin (admin.ModelAdmin):
    pass


@admin.register(Offer)
class CreditAdmin (admin.ModelAdmin):
    pass


@admin.register(OfferComment)
class CreditAdmin (admin.ModelAdmin):
    pass
