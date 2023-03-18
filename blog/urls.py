from django.urls import path
from .views import PostList, CategoryPostList, PostDetail


urlpatterns = [
    path('', PostList.as_view(), name="list"),
    path('news/<slug:slug>/', PostDetail.as_view(), name="detail"),
    path('cats/<slug:slug>/', CategoryPostList.as_view(), name="post_cat")
]
