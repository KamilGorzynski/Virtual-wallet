import random

from django.contrib.auth.models import User, Group

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from wallets.serializers import UserSerializer, GroupSerializer, WalletSerializer
from wallets.models import Wallet, CompanyData
from wallets.common import get_zus_amount, get_user
from Wallet.fin import IBAN_PREFIX
from Wallet.errors import LowerZeroError, ChangeAccountNumberError


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class WalletViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows active wallets to be viewed or edited.

    """
    serializer_class = WalletSerializer

    def get_queryset(self):
        """
        Check, if ulr contains query param country

        :return: all active wallets
        """
        country = self.request.query_params.get('country')
        if country:
            active_wallets = Wallet.objects.filter(active=True).filter(country=country)
        else:
            active_wallets = Wallet.objects.filter(active=True)
        return active_wallets

    @staticmethod
    def create_billnumber(country):
        """
        Method generates IBAN number.

        :param country: default 'PL'
        :type country: :code:`str`
        :return: iban number
        """
        times = 26
        number = "%s" % (IBAN_PREFIX.get(country, 'PL'))
        while times > 0:
            digit = random.randint(0, 9)
            number += str(digit)
            times -= 1
        return number

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        API POST method handle for endpoint: /wallets/.
        Creates new wallet account for provided data.

        """

        data = request.data
        if float(data['ballance']) < 0:
            raise LowerZeroError()
        company_data = data.get('company_data')
        c_data = None
        if company_data:
            c_data = CompanyData.objects.create(**company_data)
        data.update({
            'user': get_user(data['user']),
            'company_data': c_data,
            'account_number': self.create_billnumber(data.get('country'))
        })
        Wallet.objects.create(**data)
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def zus_day(self, request, **kwargs):
        """
        Django action methods, charges from all wallets ZUS fee.

        """

        wallets = Wallet.objects.filter(is_company=True)
        for wallet in wallets:
            wallet.ballance = float(wallet.ballance) - get_zus_amount(wallet.company_data.company_start_date)
            wallet.save()
        return Response('Fee charged')

    def update(self, request, *args, **kwargs):
        """
        API PUT method handle for endpoint: /wallets/.
        Updates wallet account with new data.
        """
        import pdb;pdb.set_trace()
        if float(request.data.get('ballance')) <= 0:
            raise LowerZeroError()
        if request.data.get('account_number'):
            raise ChangeAccountNumberError()
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Wallet updated')
