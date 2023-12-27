from rest_framework import generics

from API.models import TestModel
from API.serializers import BlackjackSerializer


class BlackjackApiView(generics.ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = BlackjackSerializer
