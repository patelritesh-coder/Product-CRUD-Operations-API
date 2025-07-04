from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_approved = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits= 10, decimal_places= 2)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name