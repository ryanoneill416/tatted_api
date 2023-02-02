from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model in order to implementa boolean field set for
    tattoo artists
    """

    def create_user(self, username, password, is_artist, **extra_fields):
        """
        Create and save a User instance with the given values
        """
        if not username:
            raise ValueError("Username is required")
        if not password:
            raise ValueError("Password is required")

        user = self.model(
            username=username,
            is_artist=is_artist,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, is_artist, **extra_fields):
        """
        Create and save a superuser with the given values
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser mst have is_superuser=True')
        return self.create_user(username, password, is_artist, **extra_fields)
