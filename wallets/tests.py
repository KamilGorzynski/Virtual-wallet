from Wallet.tests import BaseTestWithWallets

from wallets.common import get_wallet_by_account_number

from wallets.models import Wallet, CompanyData

from wallets.serializers import WalletSerializer


class ZusDayTest(BaseTestWithWallets):
    url = '/wallets/zus_day/'

    def test_zus_day_method(self):
        # ballances before:
        # younger company
        self.assertEqual(
            get_wallet_by_account_number('PL16106002781867070139336857').ballance,
            2000
        )
        # older company
        self.assertEqual(
            get_wallet_by_account_number('PL24124064497928530060117185').ballance,
            2000
        )
        # not company
        self.assertEqual(
            get_wallet_by_account_number('PL02393585864848127098076598').ballance,
            500
        )

        response = self.client.post(self.url, {}, format='json')
        self.failUnlessEqual(response.status_code, 200)
        self.assertEqual(response.data, 'Fee charged')

        # ballances after:
        self.assertEqual(
            float(get_wallet_by_account_number('PL16106002781867070139336857').ballance),
            1480.06
        )
        self.assertEqual(
            float(get_wallet_by_account_number('PL24124064497928530060117185').ballance),
            683.03
        )
        self.assertEqual(
            get_wallet_by_account_number('PL02393585864848127098076598').ballance,
            500
        )


class UpdateWalletTest(BaseTestWithWallets):
    url = '/wallets/5/'

    request = {
        'id': 5,
        'user': 3,
        'account_number': None,
        'country': 'Poland',
        'ballance': 2000,
        'creation_date': '2019-08-30 20:02:15.0000000',
        'active': True,
        'is_company': False,
        'company_data': {
            "nip": 1152702553,
            "regon": 377921888,
            "company_start_date": "2016-09-02T16:01:41Z"
        },
    }

    def get_wallet_company_data(self):
        return Wallet.objects.get(id=5).company_data

    def get_company_data_by_nip(self, nip):
        try:
            c_data = CompanyData.objects.get(nip=nip)
        except:
            c_data = None
        return c_data

    def test_update_company_data_1(self):
        """Create CompanyData object while update wallet data"""

        # No company data before update for this wallet
        self.assertEqual(self.get_wallet_company_data(), None)
        self.assertEqual(self.get_company_data_by_nip(1152702553), None)

        response = self.client.put(self.url, self.request, format='json')
        self.failUnlessEqual(response.status_code, 200)

        # Company data after update
        self.assertEqual(self.get_wallet_company_data().id, 3)
        self.assertEqual(self.get_company_data_by_nip(1152702553).nip, 1152702553)

    def test_update_company_data_2(self):
        """Modify CompanyData object while update wallet data"""

        # create company data for user
        self.client.put(self.url, self.request, format='json')

        # Company data before update for this wallet
        self.assertEqual(self.get_wallet_company_data().id, 3)
        self.assertEqual(self.get_company_data_by_nip(1152702553).nip, 1152702553)

        self.request['company_data'] = {
                "nip": 1152701111,
                "regon": 377921888,
                "company_start_date": "2016-09-02T16:01:41Z"
            }
        response = self.client.put(self.url, self.request, format='json')
        self.failUnlessEqual(response.status_code, 200)

        # Company data after update
        self.assertEqual(self.get_wallet_company_data().id, 3)
        self.assertEqual(self.get_company_data_by_nip(1152701111).nip, 1152701111)

    def test_update_company_data_3(self):
        """Delete CompanyData object while update wallet data"""

        # create company data for user
        self.client.put(self.url, self.request, format='json')

        # Company data before update for this wallet
        self.assertEqual(self.get_wallet_company_data().id, 3)
        self.assertEqual(self.get_company_data_by_nip(1152701111).nip, 1152701111)

        self.request['company_data'] = None

        response = self.client.put(self.url, self.request, format='json')
        self.failUnlessEqual(response.status_code, 200)

        # Company data after update
        self.assertEqual(self.get_wallet_company_data(), None)
        self.assertEqual(self.get_company_data_by_nip(1152701111), None)


class EnglishWalletTest(BaseTestWithWallets):
    url = '/wallets/?country=England'

    def test_get_query_params(self):
        response = self.client.get(self.url, format='json')
        english_wallets = Wallet.objects.filter(country='England')
        serializer = WalletSerializer(english_wallets, many=True)
        self.failUnlessEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)


class CRUDWalletTest(BaseTestWithWallets):
    url = '/wallets/'

    def test_crud_1(self):
        """ Create Test """
        request = {
            "user": 1,
            "ballance": "12345678",
            "creation_date": "2019-08-30T20:02:15Z",
            "active": True,
            "country": "Poland",
            "is_company": False,
            "company_data": {
                'nip': '444270255',
                'regon': '444921888',
                'company_start_date': '2016-09-02 16:01:41.0000000'
            }
        }
        response = self.client.post(self.url, request, format='json')
        self.failUnlessEqual(response.status_code, 201)
        serializer = WalletSerializer(Wallet.objects.last(), many=False)
        self.assertEqual(float(serializer.data.get('ballance')), 12345678)
        self.assertEqual(CompanyData.objects.last().regon, 444921888)

    def test_crud_2(self):
        """ Delete Test """
        request = {
            "user": 1,
            "ballance": "12345678",
            "creation_date": "2019-08-30T20:02:15Z",
            "active": True,
            "country": "Poland",
            "is_company": False,
            "company_data": {
                'nip': '444270255',
                'regon': '444921888',
                'company_start_date': '2016-09-02 16:01:41.0000000'
            }
        }
        wallet_id = Wallet.objects.last().id
        response = self.client.delete(self.url + str(wallet_id) + '/', request, format='json')
        self.failUnlessEqual(response.status_code, 204)
        wallet_list = Wallet.objects.filter(id=wallet_id)
        self.assertEqual(len(wallet_list), 0)
