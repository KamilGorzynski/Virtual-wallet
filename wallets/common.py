from django.contrib.auth.models import User
from django.db import connection

from Wallet.fin import ZUS_AMOUNTS

from datetime import datetime, timezone

from wallets.models import Wallet


def get_zus_amount(start_date):
    today = datetime.now(timezone.utc)
    return ZUS_AMOUNTS['minor_zus'] if (today - start_date).days < 730 else ZUS_AMOUNTS['major_zus']


def get_user(user_id):
    return User.objects.get(id=user_id)


def get_wallet_by_account_number(number):
    return Wallet.objects.get(account_number=number)


def get_all_ids(model):
    objects = model.objects.all()
    return [object.id for object in objects]


def get_model_by_id(model, model_id):
    return model.objects.get(id=model_id)


def not_exist(model, field, value):
    def get_table_name(model):
        return '{package_name}_{model_name}'.format(
            package_name=model.__module__.split('.')[0].lower(),
            model_name=model.__name__.lower()
        )
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT count(0) FROM {table} WHERE {field} = \'{value}\''.format(
                table=get_table_name(model),
                field=field,
                value=value
            )
        )
        return cursor.fetchone()[0] == 0


def get_all_from_table(model):
    return model.objects.all()
