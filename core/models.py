from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=500)


class Product(models.Model):
    title = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='products/', null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    details = models.CharField(max_length=19200, null=True)




