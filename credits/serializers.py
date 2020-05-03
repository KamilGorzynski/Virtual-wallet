from rest_framework import serializers
from .models import Credit


class CreditDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        exclude = ('id',)


class OfferAvgRate(object):

    def __init__(self, offer_name, avg_rate):
        self.offer_name = offer_name
        self.avg_rate = avg_rate


class OfferAvgRateSerializer(serializers.Serializer):
    offer_name = serializers.CharField(max_length=200)
    avg_rate = serializers.IntegerField()
