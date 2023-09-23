from django.db import models
from user import models as userModel
from master import models as masterModel
from django.utils.timezone import now
from safedelete.models import SafeDeleteModel, HARD_DELETE_NOCASCADE, SOFT_DELETE

class UserStore(models.Model):
    _safedelete_policy = SOFT_DELETE

    store_name = models.CharField(blank=False, max_length=50)
    owner = models.ForeignKey(userModel.OwnerAndUser, on_delete=models.CASCADE, related_name='user_store')
    status = models.ForeignKey(masterModel.Status, on_delete=models.CASCADE, related_name='status_store')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
