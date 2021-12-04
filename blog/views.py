from django.shortcuts import render

from blog.models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def blog_id(request, blog_id):
    post = Post.objects.get(id=blog_id)
    return render(request, "blog/blogid.html", {"post": post})