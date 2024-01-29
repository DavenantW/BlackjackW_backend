from rest_framework import generics

from API.models import *
from API.serializers import BlackjackSerializer


class BlackjackApiView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = BlackjackSerializer
