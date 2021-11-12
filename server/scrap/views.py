from rest_framework.response import Response
from rest_framework.views import APIView

from scrap.utils import ScrapService


class Scrap(APIView):
    def get(self, request, format=None):
        scrap_service = ScrapService()
        images = scrap_service.scrap(days=7)
        return Response(images)


