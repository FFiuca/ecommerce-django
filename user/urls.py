from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.api.views import RegisterView

router = DefaultRouter()
router.register('register', RegisterView.RegisterView, basename='register')

app_name = 'user'
urlpatterns = [
    # path('/register', RegisterView.RegisterView.as_view(), name='register'),

    path('/', include(router.urls))
]
