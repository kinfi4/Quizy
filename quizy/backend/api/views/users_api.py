from rest_framework import generics
from api.serializers.user_serializer import UserSerializer
from api.models import User


class UsersView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
