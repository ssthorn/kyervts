# from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, filters, generics, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer