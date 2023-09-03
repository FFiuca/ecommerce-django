from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserType(models.Model):
    user_type = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
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

