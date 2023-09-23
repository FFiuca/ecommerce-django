from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.api.views import RegisterView

router = DefaultRouter()
router.register('register', RegisterView.RegisterView, basename='register') # /user/auth/register
router.register('register-owner', RegisterView.RegisterOwnerView, basename='register-owner')

app_name = 'user'
urlpatterns = [
    # path('/register', RegisterView.RegisterView.as_view(), name='register'),

    path('/auth/', include(router.urls))
]
