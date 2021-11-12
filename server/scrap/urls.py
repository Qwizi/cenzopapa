from rest_framework import routes

from views import Scrap

urlpatterns = [
    path('scrap/', Scrap.as_view(), name='scrap')
]
