from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Registers Comment model in admin panel
    """
    list_display = ('username', 'is_artist')
