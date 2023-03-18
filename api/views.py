from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Category, Post
from blog.serializers import CategorySerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly



class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Category Detail"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """Post Detail"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
