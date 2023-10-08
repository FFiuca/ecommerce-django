from django.urls import include, path

from order.api.views import cart_view

app_name = 'order'
urlpatterns = [
    path('/cart', include([
        path('/list', cart_view.CartView.as_view({
            'post': 'list'
        }), name='cart-list')
    ]))
]

