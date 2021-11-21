from datetime import datetime
from random import randint

from django.contrib.auth import get_user_model
from django.db.models import Max
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from images.models import Image
from images.permissions import IsAnonCreate
from images.serializers import ImageOutSerializer


class ImageViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Image.objects.filter(is_validated=True).order_by('-posted_at')
    serializer_class = ImageOutSerializer
    permission_classes = [IsAnonCreate, ]

    def perform_create(self, serializer):
        file = self.request.data.get('file')
        serializer.save(
            author=self.request.user,
            posted_at=datetime.now(),
            file=file
        )

    @action(detail=False)
    def random(self, request):
        max_id = Image.objects.all().aggregate(max_id=Max("id"))['max_id']
        if not max_id:
            raise NotFound("Images not found")
        random_image = None
        repeat = True
        while repeat:
            try:
                pk = randint(1, max_id)
                random_image = Image.objects.get(pk=pk, is_validated=True)
                repeat = False
            except Image.DoesNotExist:
                repeat = True
        serializer = self.get_serializer(random_image)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def favorite(self, request, pk):
        image = self.get_object()
        user = self.request.user
        if user.favorite_images.filter(pk=image.pk).exists():
            raise NotFound("This image is already your favorite")
        user.favorite_images.add(image)
        return Response(data={"msg": "Successfully added image to favorites"}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def unfavorite(self, request, pk):
        image = self.get_object()
        user = self.request.user
        if not user.favorite_images.filter(pk=image.pk).exists():
            raise NotFound("This image is not in your favorites")
        user.favorite_images.remove(image)
        return Response(data={"msg": "Successfully removed image from favorites"}, status=status.HTTP_201_CREATED)
