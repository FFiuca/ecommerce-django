from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from safedelete.models import SafeDeleteModel, SOFT_DELETE

class UserType(models.Model):
    user_type = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Status(models.Model):
    status_int = models.IntegerField(blank=False)
    status_name = models.CharField(max_length=100)
    module_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['module_name', 'status_int'], name='status_rel')
        ]

class Category(
    SafeDeleteModel,
    models.Model):
    _safedelete_policy = SOFT_DELETE

    category_name = models.CharField(blank=False, max_length=255,
                                    #  unique=True // will be automatic add unique index and named as field_name. for this case will be duplicate with category_name name below
                                     )
    created_at = models.DateTimeField(blank=False, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        indexes=[
            models.Index(fields=['category_name'], name='category_name')
        ]


