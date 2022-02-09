from django.db import models
from django.contrib.auth.models import User
import datetime
class History(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    isbn=models.CharField(max_length=500)
class savedbook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    bookid=models.CharField(max_length=500)
class follower(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    following=models.CharField(max_length=500)

class Blog(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    dsc=models.TextField()
    date=models.DateTimeField(auto_now_add=True,null=True)
# Create your models here.
