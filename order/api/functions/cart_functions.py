from rest_framework import viewsets
from rest_framework import serializers
from django.db import models
from main import helpers
from store import models as mStrore
from order import models as mOrder
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

            cart = mOrder.Cart.objects.get_or_create(customer=customer, item=item)
            print(cart)
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

