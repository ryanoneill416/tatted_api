from rest_framework import generics, permissions
from tatted_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer


class ReviewList(generics.ListCreateAPIView):
    """
    List of all created review instances
    Authenticated users can create an instance relating to
    a specified 'artist'
    perform_create associates current user as 'owner'
    """

    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves a review instance
    Allows user to update or delete the instance if
    that user is the 'owner' of the instance itself
    """

    serializer_class = ReviewDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()
