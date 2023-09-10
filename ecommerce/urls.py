from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # system
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('account/', include('django.contrib.auth.urls')),

    # app
    path('user', include('user.urls')),
]
