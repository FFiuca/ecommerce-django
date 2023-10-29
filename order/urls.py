from django.urls import include, path

from order.api.views import cart_view, checkout_view, payment_view

app_name = 'order'
urlpatterns = [
    path('/cart', include([
        path('/list', cart_view.CartView.as_view({
            'post': 'list'
        }), name='cart-list'),
        path('/add', cart_view.CartView.as_view({
            'post': 'add'
        }), name='cart-add'),
        path('/async_list', cart_view.AsyncCartView.as_view(), name='item.async_list')
    ])),
    path('/checkout', include([
        path('/add', checkout_view.CheckOutView.as_view({
            'post': 'add'
        }), name='checkout-add')
    ])),
    path('/payment', include([
        path('/change_payment', payment_view.PaymentView.as_view({
            'post': 'change_payment_status'
        }), name='payment.change_payment_status')
    ])),
]

