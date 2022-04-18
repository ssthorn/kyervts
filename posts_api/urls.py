from django.urls import path
from .views import PostList, PostDetail, PostListDetailfilter, CreatePost, EditPost, AdminPostDetail, DeletePost
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'), # api/posts will be routed to the PostList view for handling
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail'), # api/posts will be routed to the PostDetail view for handling

]