from django.db import models
from django.db import models
from django.conf import settings
from posts.models import Post


class Save(models.Model):
    """
    Save model relating to 'owner' User instance
    and the 'post' model instance.
    'Unique_together' serves to ensure a user cannot
    like the same post twice
    """

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='saves')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner}: {self.post}'
