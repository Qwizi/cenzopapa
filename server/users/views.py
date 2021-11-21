from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from images.serializers import ImageOutSerializer
from users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer

    @action(detail=False, permission_classes=[IsAuthenticated])
    def favorite_images(self, request):
        favorite_images = request.user.favorite_images.filter(is_validated=True).order_by('-posted_at')
        page = self.paginate_queryset(favorite_images)
        if page is not None:
            serializer = ImageOutSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ImageOutSerializer(favorite_images, many=True)
        return Response(serializer.data)
