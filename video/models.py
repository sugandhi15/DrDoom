from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class WebUser(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be exactly 10 digits."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=10)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    last_login =  models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email