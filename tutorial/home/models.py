from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    post=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete='CASCADE')
    date=models.DateTimeField(auto_now=True)
