from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Post, Category, Tag, Comment


class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        cats = Category.objects.all()
        tags = Tag.objects.all()
        return render(request, "blog/list.html", {"posts": posts, "cats": cats, 'tags': tags})


class CategoryPostList(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        posts = Post.objects.filter(category=category)
        cats = Category.objects.all()
        tags = Tag.objects.all()
        return render(request, "blog/list.html", {"posts": posts, "cats": cats, 'tags': tags})
    

class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        cats = Category.objects.all()
        return render(request, "blog/detail.html", {"post": post, "cats": cats})
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        Comment.objects.create(name=name, email=email, text=comment, post=post)
        return redirect('detail', post.slug)
