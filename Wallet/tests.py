from django.contrib.auth.models import User
from rest_framework.test import APIClient
from unittest import TestCase


from wallets.common import get_all_from_table, get_user, get_model_by_id
from wallets.models import Wallet, CompanyData


class BaseTest(TestCase):
    """ Prepare basic set up for tests like api client instance """
    client = APIClient()

    def setUp(self):
        """ Create users for all tests """
        if not get_all_from_table(User):
            users_list = [
                {'id': 1, 'username': 'User1', 'email': 'lennon@thebeatles.com', 'password': 'johnpassword'},
                {'id': 2, 'username': 'User2', 'email': 'lennon@thebeatles.com', 'password': 'sdffsdf'},
                {'id': 3, 'username': 'User3', 'email': 'lennon@thebeatles.com', 'password': 'sdffsdf'},
                {'id': 4, 'username': 'Company1', 'email': 'lennon@thebeatles.com', 'password': 'sdffsdf'},
                {'id': 5, 'username': 'Company2', 'email': 'lennon@thebeatles.com', 'password': 'sdffsdf'},
            ]
            self.model_create(User, users_list)

    @staticmethod
    def model_create(model, params_list):
        """
            Method creates in db rows based on provided model and list of params

            :param model: class of model to create in db
            :type model: :code:`class`
            :param params_list: list of dicts containing all params
            :type params_list: :code:`list`
        """
        for params in params_list:
            model.objects.create(**params)


class BaseTestWithWallets(BaseTest):

    def setUp(self):
        """ Create wallets and company data for all tests """
        super().setUp()
        if not get_all_from_table(CompanyData):
            company_data_list = [{
                'id': 1,
                'nip': 1152702748,
                'regon': 377921239,
                'company_start_date': '2019-09-02 16:01:41.0000000',
            }, {
                'id': 2,
                'nip': 3354402750,
                'regon': 342221239,
                'company_start_date': '2016-09-02 16:01:41.0000000',
            }]
            self.model_create(CompanyData, company_data_list)
        if not get_all_from_table(Wallet):
            wallets_list = [{
                'id': 1,
                'user': get_user(1),
                'account_number': 'PL02393585864848127098076598',
                'country': 'Poland',
                'ballance': 500,
                'creation_date': '2019-08-30 20:02:15.0000000',
                'active': True,
                'is_company': False,
                'company_data': None,
            }, {
                'id': 2,
                'user': get_user(2),
                'account_number': 'EN54704858703630294860724085',
                'country': 'Poland',
                'ballance': 500,
                'creation_date': '2019-08-30 20:02:15.0000000',
                'active': True,
                'is_company': False,
                'company_data': None,
            }, {
                'id': 3,
                'user': get_user(4),
                'account_number': 'PL16106002781867070139336857',
                'country': 'Poland',
                'ballance': 2000,
                'creation_date': '2019-08-30 20:02:15.0000000',
                'active': True,
                'is_company': True,
                'company_data': get_model_by_id(CompanyData, 1),
            }, {
                'id': 4,
                'user': get_user(5),
                'account_number': 'PL24124064497928530060117185',
                'country': 'England',
                'ballance': 2000,
                'creation_date': '2019-08-30 20:02:15.0000000',
                'active': True,
                'is_company': True,
                'company_data': get_model_by_id(CompanyData, 2),
            }, {
                'id': 5,
                'user': get_user(3),
                'account_number': 'PL48102000616844247489903525',
                'country': 'England',
                'ballance': 2000,
                'creation_date': '2019-08-30 20:02:15.0000000',
                'active': True,
                'is_company': False,
                'company_data': None,
            }]
            self.model_create(Wallet, wallets_list)
