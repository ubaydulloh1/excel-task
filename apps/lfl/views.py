from rest_framework import generics
from rest_framework.permissions import AllowAny

from . import serializers, models


class LFLUploadView(generics.CreateAPIView):
    queryset = models.LFL.objects.all()
    serializer_class = serializers.LFLCreateSerializer
    permission_classes = [AllowAny]


class LFLListView(generics.ListAPIView):
    queryset = models.LFL.objects.all()
    serializer_class = serializers.LFLListSerializer
    permission_classes = [AllowAny]


class LFLDetailView(generics.ListAPIView):
    queryset = models.LFL.objects.all()
    serializer_class = serializers.LFLDetailSerializer
    permission_classes = [AllowAny]
