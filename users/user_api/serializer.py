from blog.models import custom_user
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,SerializerMethodField
class user_serializer(ModelSerializer):
    password2= serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model= custom_user
        fields=['username','email','number','password','password2']
        extra_kwargs={'password':{'write_only':True}}

        def save(self):
            store=custom_user(username=self.validated_data['username']
                              )
            password=self.validated_data['password']
            password2=self.validated_data['password2']
            email=self.validated_data['email']
            number=self.validated_data['number']

            if password == password2:
                store.set_password(password)
                store.save()
                return store
            serializers.ValidationError({'password':'password field does not match'})