from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserType(models.Model):
    user_type = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

