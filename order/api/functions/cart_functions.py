from rest_framework import viewsets
from rest_framework import serializers
from django.db import models
from main import helpers
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

