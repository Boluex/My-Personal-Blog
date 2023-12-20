from django.forms import ModelForm
from.models import profile
from blog.models import custom_user

class profile_form(ModelForm):
    class Meta:
        model=profile
        fields =['image',]

class user_form(ModelForm):
    class Meta:
        model=custom_user
        fields =['username','email','number']

