from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    dob = models.DateField()
    img = models.ImageField(default='default.svg', upload_to='profile_pics')
