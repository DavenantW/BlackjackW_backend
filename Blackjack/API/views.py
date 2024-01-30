from rest_framework.views import Response
from .models import Users
from .serializers import UsersSerializer
from rest_framework.views import APIView


class UsersApiView(APIView):
    def get(self, request):
        UsersSet = Users.objects.all()
        return Response({"all Users": UsersSerializer(UsersSet, many=True).data})
