from django.db import models
from django.conf import settings


class Review(models.Model):
    """
    Review model relatting to 'owner' as well
    as the user instance 'artist' where 'is_artist' = True
    satisfaction_ratings lets the 'owner' categorize their
    experience with the artist in question
    related_name is utilized to differentiate between both
    user instances
    """

    artists = settings.AUTH_USER_MODEL.objects.filter(is_artist=True)

    satisfaction_rating_choices = [
        ('highly recommends', 'Highly Recommend'),
        ('somewhat recommends', 'Somewhat Recommend'),
        ('does not recommend', 'Do Not Recommend'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='reviewer',
        on_delete=models.CASCADE
        )
    artist = models.ForeignKey(
        artists,
        related_name='artist',
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    satisfaction_rating = models.CharField(
        max_length=50, choices=satisfaction_rating_choices
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.satisfaction_rating}s {self.artist}'
