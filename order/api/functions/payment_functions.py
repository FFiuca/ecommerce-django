from django.db import transaction

from master import models as mMaster
from order import models as mOrder

class PaymentFunctions():

    def change_payment_status(self, checkout_code: str, status: int):
        # co = mOrder.Checkout.objects.filter(checkout_code=checkout_code).get()

        if status==2:
            return self.change_payment_to_settlement(checkout_code, status)
        elif status==3:
            return self.change_payment_to_return(checkout_code, status)

    @transaction.atomic
    def change_payment_to_settlement(self, checkout_code: str, status: int):
        payment_status = mMaster.PaymentStatus.objects.get(pk=status)
        status = mMaster.Status.objects.filter(status_name='packed', module_name='order.checkout').get()

        update = mOrder.Checkout.objects.filter(checkout_code=checkout_code).update(
            payment_status=payment_status,
            status=status
        )

        return {
            'update': update
        }

    @transaction.atomic
    def change_payment_to_return(self, checkout_code: str, status: int):
        payment_status = mMaster.PaymentStatus.objects.get(pk=status)
        status = mMaster.Status.objects.filter(status_name='retur', module_name='order.checkout').get()

        update = mOrder.Checkout.objects.filter(checkout_code=checkout_code).update(
            payment_status=payment_status,
            status=status
        )

        return {
            'update': update
        }

