from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.charField(max_length=50, null=False, blank=False)
    done = models.booleanField(max_length=50, null=False, blank=False, default=False))