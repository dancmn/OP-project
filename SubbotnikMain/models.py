from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from django.contrib.auth.models import UserManager
class UserAccount(AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=255, unique=True)
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)
    USERNAME_FIELD = 'name'  # что является логином
    objects = UserManager()
    def __str__(self):
        return self.name


class Marker(models.Model):
    markerName = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='imgs/')
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    opened = models.BooleanField(default=True, blank=True, null=True)
    signed = models.ManyToManyField(to=UserAccount, related_name="markers", blank=True, null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, blank=True, null=True, to_field="name")

    def __str__(self):
        return self.markerName
