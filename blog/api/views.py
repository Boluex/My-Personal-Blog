from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from blog.models import post,custom_user
from.serializer import detailserializer,homeserializer,createserializer
from rest_framework.generics import ListAPIView

# Create your views here.

@api_view(['GET',])
def api_detail(request,id):
    try:
        posts= post.objects.get(id=id)
    except post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serializer= detailserializer(posts)
        return Response(serializer.data)

class api_home(ListAPIView):
    queryset=post.objects.all()
    serializer_class= homeserializer


@api_view(['PUT',])
def api_update(request,id):
    try:
        posts= post.objects.get(id=id)
    except post.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer= detailserializer(posts,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['success']='Updated'
            return Response(serializer.data)
        else:
            data['success'] = 'error'
            return Response(serializer.data)


@api_view(['DELETE'])
def api_delete(request,id):
    try:
        posts=post.objects.get(id=id)
    except post.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        posts.delete()
        data={}
        data['deleted']='Deleted successfully'
        return Response(data=data)


@api_view(['POST'])
def api_create(request):
    if request.method == 'POST':
        author = custom_user.objects.get(pk=13)
        blog_post =post(author=author)
        serializer=createserializer(blog_post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)