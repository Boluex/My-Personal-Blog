from blog.models import post
from rest_framework.serializers import ModelSerializer

class detailserializer(ModelSerializer):
    class Meta:
        model=post
        fields=['id','image','title','content','date_posted']



class homeserializer(ModelSerializer):
    class Meta:
        model=post
        fields=['id','image','title','content','date_posted']

class createserializer(ModelSerializer):
    class Meta:
        model=post
        fields=['image','title','content']