from django.db import models
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        # Isso cria o link para a página do post (ex: /post/1)
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        # Garante que os posts mais novos apareçam primeiro
        ordering = ['-data_publicacao']