from Wallet.tests import BaseTestWithWallets

from wallets.common import get_wallet_by_account_number


class SimpleTransferTest(BaseTestWithWallets):
    url = '/transfers/'

    def test_transfer(self):
        request = {
            "source_account": "PL02393585864848127098076598",
            "beneficiary_account": "EN54704858703630294860724085",
            "amount": "50.00",
            "currency": "PLN",
            "title": "przelew",
            "transfer_date": "2019-09-15T20:42:11.902328Z"
        }
        response = self.client.post(self.url, request, format='json')
        self.failUnlessEqual(response.status_code, 200)

        source_wallet = get_wallet_by_account_number("PL02393585864848127098076598")
        beneficiary_wallet = get_wallet_by_account_number("EN54704858703630294860724085")
        self.assertEqual(source_wallet.ballance, 450)
        self.assertEqual(beneficiary_wallet.ballance, 550)

    def test_insufficient_funds_error(self):
        request = {
            "source_account": "PL02393585864848127098076598",
            "beneficiary_account": "EN54704858703630294860724085",
            "amount": "4000.00",
            "currency": "PLN",
            "title": "przelew",
            "transfer_date": "2019-09-15T20:42:11.902328Z"
        }
        response = self.client.post(self.url, request, format='json')
        expected_response_data = {'detail': 'Insufficient funds'}
        self.failUnlessEqual(response.data, expected_response_data)
        self.failUnlessEqual(response.status_code, 500)

    def test_lower_zero_error(self):
        request = {
            "source_account": "PL02393585864848127098076598",
            "beneficiary_account": "EN54704858703630294860724085",
            "amount": "-123.00",
            "currency": "PLN",
            "title": "przelew",
            "transfer_date": "2019-09-15T20:42:11.902328Z"
        }
        response = self.client.post(self.url, request, format='json')
        expected_response_data = {'detail': 'Amount lower than 0'}
        self.failUnlessEqual(response.data, expected_response_data)
        self.failUnlessEqual(response.status_code, 500)

    def test_beneficiary_not_exist_error(self):
        request = {
            "source_account": "PL02393585864848127098076598",
            "beneficiary_account": "1234567890",
            "amount": "3.00",
            "currency": "PLN",
            "title": "przelew",
            "transfer_date": "2019-09-15T20:42:11.902328Z"
        }
        response = self.client.post(self.url, request, format='json')
        expected_response_data = {'detail': 'beneficiary_account: 1234567890 does not exists'}
        self.failUnlessEqual(response.data, expected_response_data)
        self.failUnlessEqual(response.status_code, 500)

