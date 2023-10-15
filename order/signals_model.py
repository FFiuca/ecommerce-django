from django.db.models.signals import pre_save
from django.dispatch import receiver
from order import models

from order.api.functions import checkout_functions

@receiver(pre_save, sender=models.Checkout)
def generete_checkout_code(sender, instance, *args, **kwargs):
    if instance._state.adding:
        instance.checkout_code = checkout_functions.generate_checkout_code()
