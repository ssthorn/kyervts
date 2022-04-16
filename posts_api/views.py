from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

# Display Posts

class PostList(generics.ListAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveAPIView):

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

# Post Search

class PostListDetailfilter(generics.ListAPIView):
  
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']

# Post Admin

class CreatePost(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AdminPostDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()




# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all().order_by('id')
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all().order_by('id')
#     serializer_class = PostSerializer