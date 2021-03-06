from django.urls import include, path
from rest_framework import routers

from images.views import ImageViewSet

router = routers.SimpleRouter()
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]