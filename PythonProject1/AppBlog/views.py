from django.shortcuts import render
from .models import Post
def categoria(request, categoria):
    # implementar função obter_posts_por_categoria
    def obter_posts_por_categoria():
        posts = Post.objects.all()
        # Filtrar posts por categoria
        posts_filtrados = [post for post in posts if post.titulo == categoria]
        return posts_filtrados
    # Obter posts por categoria e renderizar a página com os posts
    posts = obter_posts_por_categoria(categoria)
    return render(request, 'AppBlog/categoria.html', {'posts': posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'AppBlog/posts_list.html', {'posts': posts})

def index(request):
    posts = Post.objects.all()
    return render(request, 'AppBlog/index.html', {'posts': posts})

def detalhe_post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'AppBlog/detalhe_post.html', {'post': post})
