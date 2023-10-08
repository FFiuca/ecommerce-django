from django.db import models
from main import auth_helpers
from main import auth_helpers

class CartQuery(models.QuerySet):
    def by_current_user(self):
        return self.filter(customer=auth_helpers.get_current_user())

class CartManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def by_current_user(self):

        if auth_helpers.get_current_user() is not None and auth_helpers.get_current_user().get.is_superuser:
            return self.get_queryset().filter(customer=auth_helpers.get_current_user().is_superuser)

        return self.get_queryset()
