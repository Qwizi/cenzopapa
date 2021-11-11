from django.urls import include, path
from rest_framework import routers

from images.views import ImageViewSet

router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]