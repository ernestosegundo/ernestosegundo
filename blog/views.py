from django.shortcuts import render

from blog.models import Post, CategoriaPost

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def blog_id(request, blog_id):
    # El post
    post = Post.objects.get(id=blog_id)

    # Las categorias del post
    categorias_post = post.categorias.all()

    posts = Post.objects.filter(categorias=categorias_post[0])
    
    return render(request, "blog/blogid.html", {"post": post, "posts": posts})

def categoria(request, categoria_id):
    categoria = CategoriaPost.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {"categoria": categoria, "posts": posts})