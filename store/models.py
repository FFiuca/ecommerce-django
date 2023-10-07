from django.db import models
from user import models as userModel
from master import models as masterModel
from order import models as oModel
from django.utils.timezone import now
from safedelete.models import SafeDeleteModel, HARD_DELETE_NOCASCADE, SOFT_DELETE


class UserStore(models.Model):
    _safedelete_policy = SOFT_DELETE

    store_name = models.CharField(blank=False, max_length=50)
    owner = models.ForeignKey(userModel.OwnerAndUser, on_delete=models.CASCADE, related_name='user_store')
    status = models.ForeignKey(masterModel.Status, on_delete=models.CASCADE, related_name='status_store')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        ordering = ['store_name']
        db_tablespace = 'user_store_test_space'
        indexes = [
            models.Index(fields=['store_name'], name='store_name')
        ]

class UserItem(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE

    item_name = models.CharField(blank=False, max_length=255)
    owner = models.ForeignKey(userModel.OwnerAndUser, on_delete=models.CASCADE, related_name='user_item_owner')
    created_at = models.DateTimeField(blank=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    # c2.useritem_set.filter(item_name__contains='item 1').get()
    # i.category.filter(category_name='cat 2').all()
    category = models.ManyToManyField(masterModel.Category,through='ItemCategory', through_fields=['item', 'category']) # https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.through_fields
    customer_cart = models.ManyToManyField(userModel.Customer, through='order.Cart', through_fields=['item', 'customer'])

    class Meta:
        db_tablespace = 'user_item_test_space'
        indexes = [
            models.Index(fields=['item_name'], name='item_name')
        ]

class UserTag(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    tag_name = models.CharField(blank=False, max_length=100)
    owner = models.ForeignKey(userModel.OwnerAndUser, on_delete=models.CASCADE, related_name='user_tag_owner')
    created_at = models.DateTimeField(blank=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    item = models.ManyToManyField(UserItem, related_name='user_tag_item') # will create pivot table automatically

    class Meta:
        db_tablespace = 'user_tag_test_space'
        indexes = [
            models.Index(fields=['tag_name'])
        ]


# custom pivot table
class ItemCategory(models.Model):
    category = models.ForeignKey(masterModel.Category, on_delete=models.CASCADE, related_name='pivot_item_category')
    item = models.ForeignKey(UserItem, on_delete=models.CASCADE, related_name='pivot_category_item')
