from rest_framework import generics
from api.models import Tag
from api.serializers.serializers import TagSerializer


class TagsView(generics.ListAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.all()
