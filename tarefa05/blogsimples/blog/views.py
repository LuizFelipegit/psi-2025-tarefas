from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    """View para a página inicial que lista todos os posts."""
    todos_os_posts = Post.objects.all()
    contexto = {'posts': todos_os_posts}
    return render(request, 'blog/index.html', contexto)

def post_detail(request, id):
    """View para a página de um post específico."""
    post = get_object_or_404(Post, id=id)
    contexto = {'post': post}
    return render(request, 'blog/post_detail.html', contexto)