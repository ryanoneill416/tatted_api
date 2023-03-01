from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'is_artist', 'date_joined', 'last_login',
                  'is_active']


class CustomRegisterSerializer(RegisterSerializer):
    """
    Custom Register Serializer needed for succesful implementation
    of the custom user in the frontend
    """

    username = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    is_artist = serializers.BooleanField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'is_artist': self.validated_data.get('is_artist', '')
        }

    def custom_signup(self, request, user):
        cleaned_data = self.get_cleaned_data()

        user.is_artist = cleaned_data['is_artist']

        user.save()

        return super().custom_signup(request, user)
