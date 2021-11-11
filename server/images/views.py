from random import randint

from django.db.models import Max
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from images.models import Image
from images.serializers import ImageOutSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.filter(is_validated=True).order_by('-posted_at')
    serializer_class = ImageOutSerializer

    @action(detail=False)
    def random(self, request):
        max_id = Image.objects.all().aggregate(max_id=Max("id"))['max_id']
        pk = randint(1, max_id)
        random_image = Image.objects.get(pk=pk)
        serializer = self.get_serializer(random_image)
        return Response(serializer.data)

