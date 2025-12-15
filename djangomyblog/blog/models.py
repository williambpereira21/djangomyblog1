# djangomyblog\blog\models.py

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3,
        choices=[('ON', 'Online'), ('OFF', 'Offline'), ('DEL', 'Deletado')],
        default='ON'
    )
    views = models.IntegerField(default=0)
    # Reservado para uso futuro
    metadata = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.CharField(
        max_length=3,
        choices=[('ON', 'Online'), ('OFF', 'Offline'), ('DEL', 'Deletado')],
        default='ON'
    )
    # Reservado para uso futuro
    metadata = models.TextField(blank=True)

    def __str__(self):
        return f'Comentário de {self.user} em {self.post.title}'