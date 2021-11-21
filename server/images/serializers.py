from rest_framework import serializers

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ImageOutSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(
        source='likes.count',
        read_only=True
    )
    class Meta:
        model = Image
        fields = ['id', 'url', 'width', 'height', 'posted_at', 'author', 'likes', 'likes_count']
        read_only_fields = ['id', 'url', 'width', 'posted_at', 'author']
        write_fields = ['file']
