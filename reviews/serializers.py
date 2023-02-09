from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializing the Review Model
    Adding extra fields for when the instance is returned
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    artist_username = serializers.ReadOnlyField(source='artist.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Review
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'artist',
            'artist_username',
            'created_at',
            'updated_at',
            'content',
            'satisfaction_rating'
        ]


class ReviewDetailSerializer(ReviewSerializer):
    """
    Will be used in the 'detail' view
    'artist' is a read_only field so it doesnt have
    to be set everytime the instance is updated
    """

    artist = serializers.ReadOnlyField(source='artist.id')
