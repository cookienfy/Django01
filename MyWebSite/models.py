from django.db import models


# Create your models here.
class tb_user(models.Model):
    Id = models.AutoField(primary_key=True)
    LoginName = models.CharField(max_length=30)
    Password = models.CharField(max_length=20)
    PetName = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
