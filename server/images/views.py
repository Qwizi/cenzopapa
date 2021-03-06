from datetime import datetime
from random import randint

from django.db.models import Max
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from images.models import Image
from images.permissions import IsAnonCreate
from images.serializers import ImageOutSerializer


class ImageViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Image.objects.filter(is_validated=True).order_by('-posted_at')
    serializer_class = ImageOutSerializer

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