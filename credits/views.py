from django.db.models import Avg

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import OfferAvgRateSerializer, CreditDataSerializer, OfferAvgRate
from .models import Credit, Offer, OfferComment
from wallets.common import get_all_ids
from Wallet.errors import NoOfferIdError


class CreditViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows credits to be viewed or edited.
    """
    queryset = Credit.objects.all()
    serializer_class = CreditDataSerializer


class OfferAvgRateViewSet(viewsets.ModelViewSet):

    def get_offer_title(self, offer_id):
        return Offer.objects.get(id=offer_id).title

    def get_avg_rate(self, offer_id):
        return (OfferComment.objects.filter(offer_id=offer_id).aggregate(Avg('rate'))).get('rate__avg')

    @action(detail=False, methods=['post'])
    def avg(self, request):
        offer_id = request.data.get('offer_id')
        if int(offer_id) not in get_all_ids(Offer):
            raise NoOfferIdError(offer_id)
        offer_info = OfferAvgRate(
            offer_name=self.get_offer_title(offer_id),
            avg_rate=self.get_avg_rate(offer_id)
        )
        serializer = OfferAvgRateSerializer(offer_info, many=False)
        return Response(serializer.data)
