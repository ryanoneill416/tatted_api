from django.db import models
from django.conf import settings


class Post(models.Model):
    """
    Post model relating to 'artist', i.e. a User instance in
    wich is_artist = True.
    Default image set so that image.url will be referenced successfully
    """

    style_choices = [
        ('traditional', 'Traditional'),
        ('neo-traditional', 'Neo-Traditional'),
        ('japanese', 'Japanese'),
        ('realism', 'Realism'),
        ('fineline', 'Fineline'),
        ('blackwork', 'Blackwork'),
        ('color', 'Color'),
        ('script', 'Script'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ifegan', blank=True)
    content = models.TextField()
    style = models.CharField(
        max_length=50, choices=style_choices, default='other')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}: {self.style} post {self.id}'
