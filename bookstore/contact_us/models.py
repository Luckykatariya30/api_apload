from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    reviews = models.TextField( null=True, blank=True)
