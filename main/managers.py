from django.db import models

class ActiveModelManager(models.Manager):
    def active(self):
        return self.filter(active=True)