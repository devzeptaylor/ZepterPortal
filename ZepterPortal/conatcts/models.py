from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Telefon(models.Model):
    fio = models.CharField(max_length=255)
    tel = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)

