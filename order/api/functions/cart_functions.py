from rest_framework import viewsets
from rest_framework import serializers
from django.db import models
from main import helpers
from store import models as mStrore
from order import models as mOrder
from user import models as mUser
from master import models as mMaster
from django.db.models import Q

class CartFunctions():
    def list(self: viewsets, serializer: serializers,
             query: models, data):
        try:
            q = Q()
            # print(query.all())
            # if not self.request.user.is_superuser:
            #     query = query.by_current_user()

            if data.get('item'):
                q = Q(item=data['item'])

            query = query.select_related('customer', 'item', 'status').filter(q)
            print(query.query)
            serializer = serializer(query, many=True).data
        except Exception as e:
            return {
                'status': 500,
                'data' : {
                    'error': helpers.messageError(e)
                }
            }

        return {
            'status': 200,
            'data': serializer
        }

    def add_to_cart(self: viewsets, query: models, data):
        add = None
        try:
            item = mStrore.UserItem.objects.filter(id=data['item']).first()
            customer = self.request.user.customer
            qty = data['qty']
            status = mMaster.Status.objects.get(pk=9)

            print(item, customer, mUser.Customer.objects.get(pk=customer.pk))

            cart, created = mOrder.Cart.objects.filter(customer=customer.pk, item=item.pk, status__in=(9,10,)).get_or_create(customer=customer, item=item, status=status)
            print(cart, created)
            if cart.status_id==0:
                cart.status_id = 1
                cart.qty = 0

            cart.qty+= qty

            add = cart.save()

        except Exception as e:
            return {
                'status': 500,
                'data' : {
                    'error': helpers.messageError(e)
                }
            }

        return {
            'status': 200,
            'data': add
        }

