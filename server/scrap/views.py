from rest_framework.response import Response
from rest_framework.views import APIView
from django_q.tasks import AsyncTask
from scrap.utils import ScrapService


class Scrap(APIView):
    def get(self, request, format=None):

        scrap_service = ScrapService()
        a = AsyncTask(scrap_service.scrap, 365, 2)
        a.run()
        print(a.result(wait=1))
        return Response(None)


