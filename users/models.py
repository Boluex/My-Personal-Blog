from django.db import models
from blog.models import custom_user
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(custom_user,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='images')

   
