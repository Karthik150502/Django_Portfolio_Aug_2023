from django.db import models
from django.contrib.auth.models import User


# # Create your models here.




class emailform(models.Model):
    username = models.CharField(max_length = 200)
    email = models.EmailField()





