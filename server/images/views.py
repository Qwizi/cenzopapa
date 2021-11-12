from random import randint

from django.db.models import Max
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, never_cache
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from images.models import Image
from images.serializers import ImageOutSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.filter(is_validated=True).order_by('-posted_at')
    serializer_class = ImageOutSerializer

    """
    @method_decorator(cache_page(60 * 1))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    """


    @never_cache
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
