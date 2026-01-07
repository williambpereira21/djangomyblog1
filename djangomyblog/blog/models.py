from django.db import models
from django.conf import settings

STATUS_CHOICES = [
    ('ON', 'Online'),
    ('OFF', 'Offline'),
    ('DEL', 'Deletado'),
]

class Post(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='ON',
        db_index=True
    )
    views = models.PositiveIntegerField(default=0)
    metadata = models.JSONField(null=True, default=dict, blank=True)  # reservado para uso futuro

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)  # comentário de post (opcional)
    page = models.CharField(max_length=50, blank=True, null=True)  # comentário de página, ex: 'sobre'
    comment = models.TextField()
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='ON',
        db_index=True
    )
    metadata = models.JSONField(null=True, default=dict, blank=True)  # reservado para uso futuro

    def __str__(self):
        target = f'post #{self.post.id}' if self.post else f'página {self.page}'
        return f'Comentário #{self.id} por {self.user} em {target}'
