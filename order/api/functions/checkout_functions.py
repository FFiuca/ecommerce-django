from django.db import transaction
from django.forms.models import model_to_dict

from master import models as mMaster
from user import models as mUser
from store import models as mStore
from order import models as mOrder

import datetime

class CheckOutFunctions:
    def __init__(self, customer2: mUser.Customer, *args, **kwargs):
        self.customer = customer2

    @transaction.atomic
    def add(self, data: dict, item: list):
        data['customer'] = self.customer
        data['user_store']= mStore.UserStore.objects.get(pk=data['user_store'])
        data['payment_method'] = mMaster.PaymentMethod.objects.get(pk=data['payment_method'])
        
        co = mOrder.Checkout.objects.create(**data)
        print('sini', co)
        detail = []
        for idx, r in enumerate(item):
            print('ttt',r)
            detail.append(mOrder.CheckoutDetail(qty=r['qty'], item=mStore.UserItem.objects.get(pk=r['item'])))

        detail = mOrder.CheckoutDetail.objects.bulk_create(detail)
        print(detail, co)

        return {
            'co': model_to_dict(co),
            # 'detail': detail
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
