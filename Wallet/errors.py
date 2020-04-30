from rest_framework.exceptions import APIException


class BaseError(APIException):

    def __init__(self):
        self.detail = self.get_details_response()

    def get_details_response(self):
        raise NotImplementedError()


class BeneficiaryNotExistError(BaseError):

    def __init__(self, beneficiary):
        self.detail = self.get_details_response(beneficiary)

    def get_details_response(self, beneficiary):
        return 'beneficiary_account: {} does not exists'.format(beneficiary)


class LowerZeroError(BaseError):

    def get_details_response(self):
        return 'Amount lower than 0'


class InsufficientFundsError(BaseError):

    def get_details_response(self):
        return 'Insufficient funds'


class NoOfferIdError(BaseError):

    def __init__(self, offer_id):
        self.detail = self.get_details_response(offer_id)

    def get_details_response(self, offer_id):
        return 'offer_id: {} does not exists'.format(offer_id)


class ChangeAccountNumberError(BaseError):

    def get_details_response(self):
        return 'Account number change not allowed'
