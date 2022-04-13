from django.urls import path
from . import views

urlpatterns = [
    path('api/posts', views.PostList.as_view(), name='post_list'), # api/posts will be routed to the PostList view for handling
    path('api/posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'), # api/posts will be routed to the PostDetail view for handling
]