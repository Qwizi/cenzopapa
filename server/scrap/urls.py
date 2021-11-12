from django.urls import path

from scrap.views import Scrap

urlpatterns = [
    path('scrap/', Scrap.as_view(), name='scrap')
]
