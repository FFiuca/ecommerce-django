from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from order import models as mOrder
from django.core.mail import send_mail
from django.conf import settings
from django_q.tasks import async_task
from order.api.functions import checkout_functions

print('discovered')

def send_mail_co2(data):
    print('tasks run new')
    # mail sended
    send =send_mail(
            "CO has created by Task",
            data.checkout_code+' task',
            settings.EMAIL_FROM_ADDRESS,
            [
                'fardana.fiuca31@gmail.com'
            ],
            fail_silently=False,
        )

    print('send async', send)

@receiver(pre_save, sender=mOrder.Checkout)
def generete_checkout_code(sender, instance, *args, **kwargs):
    print('signal co generate_code', sender, instance, instance._state, args, kwargs)
    if instance._state.adding:
        instance.checkout_code = checkout_functions.generate_checkout_code()

@receiver(post_save, sender=mOrder.Checkout)
def send_mail_checkout(sender, instance, created, *args, **kwargs):
    print('signal co send mail', sender, instance, instance._state, created, args, kwargs)
    if created :
        # can't send yet, check it later, but when using shell success
        send =send_mail(
            "CO has created by Signal",
            instance.checkout_code,
            settings.EMAIL_FROM_ADDRESS,
            [
                'fardana.fiuca31@gmail.com'
            ],
            fail_silently=False,
        )
        print('send', send, settings.EMAIL_FROM_ADDRESS, instance.checkout_code)

        # do with async task
        task = async_task(send_mail_co2, instance)
        print('task new', task)
