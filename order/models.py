from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from user import models as uModel
from store import models as sModel
from master import models as mModel
from order import model_managers

class Cart(models.Model):
    _safedelete_policy = SOFT_DELETE

    customer = models.ForeignKey(uModel.Customer, related_name='cart_customer', on_delete=models.CASCADE)
    item = models.ForeignKey(sModel.UserItem, related_name='cart_item', on_delete=models.CASCADE)
    status = models.ForeignKey(mModel.Status, related_name='cart_status', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    # for scoping like laravel
    objects = model_managers.CartManager()

    class Meta:
        ordering = ['created_at']
