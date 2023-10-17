from django.db import transaction

from master import models as mMaster
from user import models as mUser
from store import models as mStore
from order import models as mOrder

import datetime

class CheckOutFunctions:
    def __init__(self, customer2: object, *args, **kwargs):
        self.customer = customer2

    @transaction.atomic
    def add(self, data: dict, item: list):
        data['customer'] = self.customer
        co = mOrder.Checkout.objects.create(**data)

        detail = []
        for idx, r in item:
            detail[idx] = mOrder.CheckoutDetail(qty=r['qty'], item=mStore.UserItem.objects.get(pk=r['item']))

        detail = mOrder.CheckoutDetail.objects.bulk_create(detail)

        return {
            'co': co,
            'detail': 'detail'
        }

def generate_checkout_code():
    count = mOrder.Checkout.objects.count()
    count+= 1

    date = datetime.datetime.now()

    return 'CO-{}{}-{}'.format(
        date.year,
        date.month,
        f'{count:03}'
    )
