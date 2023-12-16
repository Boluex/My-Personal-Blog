from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils import timezone
# Create your models here.
class custom_user(AbstractUser):
       number = models.CharField(max_length=12)

class post(models.Model):
    author=models.ForeignKey(custom_user,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post')
    title=models.CharField(max_length=50)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)

class comment(models.Model):
    author=models.ForeignKey(custom_user,on_delete=models.CASCADE)
    posts=models.ForeignKey(post,on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    date_posted=models.DateTimeField(auto_now_add=True)