from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from blog.models import custom_user
from.serializer import user_serializer

# Create your views here.
@api_view(['POST',])
def login(request):
    if request.method == 'POST':
        serializer=user_serializer(custom_user,data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='Account created successfully'
            data['email']=account.email
            data['username']=account.username
            return Response(data=data)
        Response(serializer.errors)