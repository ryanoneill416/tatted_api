from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from tatted_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """"
    List of all profile instances
    Profile creation handled by django signals
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve profile detail view.
    User is allowed to update the profile if they are 'owner'
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
