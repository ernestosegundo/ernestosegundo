from django.shortcuts import render

from blog.models import Post, CategoriaPost

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def blog_id(request, blog_id):
    post = Post.objects.get(id=blog_id)

    posts_relacionados = []
    for categoria_post in post.categorias.all():
        posts_relacionados += Post.objects.filter(categorias=categoria_post)
    
    for el_post in posts_relacionados:
        if el_post.titulo == post.titulo:
            posts_relacionados.remove(el_post)
    
    return render(request, "blog/blogid.html", {"post": post, "posts_relacionados": posts_relacionados})

def categoria(request, categoria_id):
    categoria = CategoriaPost.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {"categoria": categoria, "posts": posts})