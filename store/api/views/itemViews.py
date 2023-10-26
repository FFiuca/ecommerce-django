from rest_framework import viewsets, views, mixins
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.http import request
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from store.models import UserItem
from django.db.models import Q
from store.api.serializers import ItemSerializers # . present for current level folder
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class ItemView(viewsets.ModelViewSet):
    queryset = UserItem.objects.all()
    serializer_class = ItemSerializers.ItemSerializer

    @action(detail=False, methods=['POST', 'GET'])
    @method_decorator(cache_page(timeout=60* 1))
    def list(self, request, *args, **kwargs):
        cond = Q()
        req = request.data
        if req.get('item_name') is not None :
            cond= cond & Q(item_name__contains=req['item_name'])

        if req.get('category_id') is not None:
            cond = cond & Q(category__id=req['category_id'])

        if req.get('tag_id'):
            cond = cond & Q(user_tag_item__id=req['tag_id'])

        query = self.get_queryset().prefetch_related('category', 'user_tag_item').filter(cond) # need optimazation for user_tag_item due not use where in clause when get data

        data = self.get_serializer(query, many=True).data
        data = {
            'status': 200,
            'data': data
        }

        return Response(data=data, status=data['status'])

@csrf_exempt
@api_view(['GET', 'POST'])
def search(request):
        print('cokkkk')
        queryset = UserItem.objects.all()
        # serializer_class = ItemSerializers
        data = ItemSerializers.ItemSerializer(queryset, many=True).data
        # data = self.get_serializer(self.get_queryset(), many=True)
        data = {
            'status': 200,
            'data': data
        }

        return Response(data=data, status=data['status'])
