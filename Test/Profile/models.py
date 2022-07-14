
from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField
    gender = models.CharField(max_length=100)
    ph = models.IntegerField



