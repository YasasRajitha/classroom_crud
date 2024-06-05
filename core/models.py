from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    re_password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10,
                             validators=[RegexValidator(r'^[0-9]+$','Enter a Valid Phone Number')]
                             )