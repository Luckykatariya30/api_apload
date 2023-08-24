from django.db import models

# Create your models here.

class Registre(models.Model):
    User_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Contect_No = models.IntegerField()
    address = models.TextField()

    class Meta:
        ordering = ['User_Name']