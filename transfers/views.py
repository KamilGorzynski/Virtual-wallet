from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import Transfer
from wallets.models import Wallet
from wallets.common import get_wallet_by_account_number
from Wallet.errors import (
    BeneficiaryNotExistError,
    LowerZeroError,
    InsufficientFundsError,
)


class TransferViewSet(viewsets.ModelViewSet):

    def transfer_saldo_changes(self, source_account, beneficiary_account, amount):
        source_wallet = get_wallet_by_account_number(source_account)
        beneficiary_wallet = get_wallet_by_account_number(beneficiary_account)
        if source_wallet.ballance < amount:
            raise InsufficientFundsError()
        source_wallet.ballance = float(source_wallet.ballance) - amount
        source_wallet.save()
        beneficiary_wallet.ballance = float(beneficiary_wallet.ballance) + amount
        beneficiary_wallet.save()

    def create(self, request, *args, **kwargs):
        data = request.data
        source_acc = data.get('source_account')
        beneficiary_acc = data.get('beneficiary_account')
        amount = float(data.get('amount')) or 0
        if amount <= 0:
            raise LowerZeroError()
        if not Wallet.objects.filter(account_number=beneficiary_acc):
            raise BeneficiaryNotExistError(beneficiary_acc)
        self.transfer_saldo_changes(source_acc, beneficiary_acc, amount)
        Transfer.objects.create(
            source_account=source_acc,
            beneficiary_account=beneficiary_acc,
            amount=amount,
            currency=data.get('currency'),
            title=data.get('title')
        )
        return Response(status=status.HTTP_200_OK)

