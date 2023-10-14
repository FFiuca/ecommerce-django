from django.db import models

# one class manager should only single purpose and have 1 method only: get_queryset
# so best practice is used for agregate purpose
# https://medium.com/@sandesh.thakar18/model-managers-in-django-6e04ccd5b3
class StatusManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def by_module_name(self, name: str):
        return self.get_queryset().filter(module_name=name)

    def by_status_int(self, status: int):
        return self.get_queryset().filter(status_int=status)
