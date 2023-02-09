from django.db import models
from django.conf import settings


class Follower(models.Model):
    """
    Follower model relating to 'owner' and 'followed'
    user instances. 'owner' is the user that is following
    and 'followed' is the user being followed by 'owner.
    related_name is used to differentiate the user model insances.
    'unique_together' ensures no duplicates are created
    """

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='follower',
        on_delete=models.CASCADE
        )
    followed = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='followed',
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['owner', 'followed']
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}: {self.followed}'
