from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from user import models as uModel
from store import models as sModel
from master import models as mModel

class Cart(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    customer = models.ForeignKey(uModel.Customer, related_name='chart_customer', on_delete=models.CASCADE)
    item = models.ForeignKey(sModel.UserItem, related_name='chart_item', on_delete=models.CASCADE)
    status = models.ForeignKey(mModel.Status, related_name='chart_status', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        ordering = ['created_at']
