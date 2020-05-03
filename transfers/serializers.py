from rest_framework import serializers

from .models import Transfer


class TransfersDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        exclude = ('id',)
