from django.db import models
from master import models as masterModel
from store import models as storeModel

class ItemCategory(models.Model):
    category = models.ForeignKey(masterModel.Category, related_name='pivot_item_category')
    item = models.ForeignKey(storeModel, related_name='pivot_category_item')
