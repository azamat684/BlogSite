from django.urls import path
from .views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('cats/', CategoryListCreateAPIView.as_view(), name="cats"),
    path('cat/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="cat_detail"),
    path('posts/', PostListCreateAPIView.as_view(), name="posts"),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name="post_detail")

]


