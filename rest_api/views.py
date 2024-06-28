from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins

from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class PostViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
   serializer_class=PostSerializers
   queryset=Post.objects.all()
   


class genericApiView(generics.GenericAPIView,
mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
   

   serializer_class=PostSerializers
   queryset=Post.objects.all()
   lookup_field='id'
   authentication_classes=[SessionAuthentication,BasicAuthentication]
   permission_classes=[IsAuthenticated]
   def get(self,request):
      if id:
         return self.retrieve(request)
      else:

         
        return self.list(request)
   def post(self,request):
      return self.create(request)
   def put(self,request,id=None):
      return self.update(request,id)
   def delete(self,request,id=None):
      return self.destroy(request,id)

class PostAPIView(APIView):
   def get(self,request):
      posts = Post.objects.all()
      serializer = PostSerializers(posts,many=True)
      return Response(serializer.data)
   
   def post(self,request):
      serializer= PostSerializers(data=request.data)

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      



@api_view(['GET','POST'])
def PostsView(request):
   if request.method=='GET':
      posts = Post.objects.all()
      serializer = PostSerializers(posts,many=True)
      return Response(serializer.data)
   
   elif request.method=='POST':
      
      serializer= PostSerializers(data=request.data)

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
      
class postdetailAPIView(APIView):
   def get_object(self,pk):
      try:
         return Post.objects.get(pk=pk)
      except Post.DoesNotExist:
         raise Http404
      
   def get(self,request,pk):
      post=self.get_object(pk)
      serializer =PostSerializers(post)
      return Response(serializer.data)
   def put(self,request,pk):
      post=self.get_object(pk)
      serializer = PostSerializers(post,data=request.data)

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

   def delete(self,request,pk):
      post=self.get_object(pk)
      post.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])

def posts_detail(request,pk):
   try:
      post=Post.objects.get(pk=pk)
   except post.DoesNotExist:
      return Response(status=404)
   
   if request.method == 'GET':
      serializer =PostSerializers(post)
      return Response(serializer.data)
   elif request.method =='PUT':
      
      serializer = PostSerializers(post,data=request.data)

      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors,status=400)
   
   elif request.method=='DELETE':
      post.delete()
      return Response(status=204)
   
   
