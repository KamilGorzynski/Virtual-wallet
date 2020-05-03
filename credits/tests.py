from .models import Offer, OfferComment
from wallets.common import get_all_from_table, get_user
from Wallet.tests import BaseTest


class OfferAvgRateTest(BaseTest):
    url = '/offer_rate/avg/'

    def setUp(self):
        super().setUp()
        offer1 = Offer.objects.create(title='Offer1', text='lorem ipsum')
        if not get_all_from_table(OfferComment):
            offer_comments_list = [
                {'offer': offer1, 'rate': 1, 'comment': 'comment', 'author': get_user(1)},
                {'offer': offer1, 'rate': 9, 'comment': 'comment', 'author': get_user(2)},
                {'offer': offer1, 'rate': 2, 'comment': 'comment', 'author': get_user(3)},
            ]
            self.model_create(OfferComment, offer_comments_list)

    def test_avg_rate(self):
        request = {'offer_id': 1}
        response = self.client.post(self.url, request, format='json')
        expected_response_data = {
            "offer_name": "Offer1",
            "avg_rate": 4
        }
        self.failUnlessEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_response_data)

    def test_no_offer_id_error(self):
        request = {'offer_id': 6}
        response = self.client.post(self.url, request, format='json')
        expected_response_data = {
            'detail': 'offer_id: 6 does not exists'
        }
        self.assertEqual(response.data, expected_response_data)
