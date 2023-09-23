from django.db import models
from django.contrib.auth.models import User
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE, SOFT_DELETE

from master import models as modelsMaster

class Customer(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    mobile_phone = models.CharField(max_length=25, blank=True)
    customer_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    usertype  = models.ForeignKey(modelsMaster.UserType, on_delete=models.CASCADE, related_name='usertype')
    status = models.ForeignKey(modelsMaster.Status, on_delete=models.CASCADE, related_name='status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OwnerAndUser(
    SafeDeleteModel,
    models.Model
    ):
    # _safedelete_policy = SOFT_DELETE

    mobile_phone = models.CharField(max_length=25, blank=True)
    owner_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype  = models.ForeignKey(modelsMaster.UserType, on_delete=models.CASCADE
                                #   , related_name='usertype' # can't duplicate with others even different model
                                  )
    status = models.ForeignKey(modelsMaster.Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
