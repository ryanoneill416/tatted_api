from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from tatted_api.permissions import IsArtistOrReadOnly, IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List of all post instances.
    Logged in users who are artists can create posts
    The perform_create method associates post with user
    """

    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsArtistOrReadOnly
    ]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retreive the post detail view
    Editing and deletion is permitted only for 'owner'
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
