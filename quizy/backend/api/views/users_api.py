from rest_framework import generics
from api.serializers.serializers import UserSerializer
from api.models import User


class UsersView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
