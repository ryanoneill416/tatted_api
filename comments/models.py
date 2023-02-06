from django.db import models
from django.conf import settings
from posts.models import Post


class Comment(models.Model):
    """
    Comment model relating to 'owner', the creator
    of the comment and the 'post' in which it is
    referring to
    """

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}: {self.content}'
