from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.api.views import RegisterView, LoginView

router = DefaultRouter()
router.register('register', RegisterView.RegisterView, basename='register') # /user/auth/register
router.register('register-owner', RegisterView.RegisterOwnerView, basename='register-owner')

app_name = 'user'
urlpatterns = [
    # path('/register', RegisterView.RegisterView.as_view(), name='register'),

    path('/auth/', include(router.urls)),

    path('/login', include([
        path('/login-customer', LoginView.LoginView.as_view({'post': 'login_customer'}), name='login-customer'),
        path('/login-owner', LoginView.LoginView.as_view({'post': 'login_owner'}), name='login-owner')
    ]), name='login'), # name from parent doesnt effect, use in child name
]
