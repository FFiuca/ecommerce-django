from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.api.views import itemViews

router = DefaultRouter()
router.register('item2', itemViews.ItemView, basename='item2')

app_name = 'store'
urlpatterns = [
    # path('/', include(router.urls)),

    path('/item', include([
        path('/list', itemViews.ItemView.as_view({
            'post': 'list',
            'get': 'list'
            }), name='item.list'),
        path('/search2', itemViews.search, name='item.list'),
    ]), name='item')
]

