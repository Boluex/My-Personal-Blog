from django.db import models
from blog.models import custom_user
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(custom_user,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='images')
    location =models.CharField(max_length=100,null=True,blank=True,default='')
    about=models.CharField(max_length=1000,null=True,blank=True,default='')
    business_info=models.CharField(max_length=2000,null=True,blank=True,default='')
    business_link=models.URLField(null=True,blank=True,default='')
