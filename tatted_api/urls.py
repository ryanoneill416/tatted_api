from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route, CustomRegisterView

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('register/', CustomRegisterView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include('profiles.urls')),
    path('', include('users.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('saves.urls')),
    path('', include('followers.urls')),
    path('', include('reviews.urls')),
]
