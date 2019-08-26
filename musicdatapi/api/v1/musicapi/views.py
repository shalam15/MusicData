from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Music
from .serializers import MusicSerializer

class MusicView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

# class MusicViews(APIView):
#     def get(self, request):
#         musics = Music.objects.all()
#         return Response({"articles": musics})

#     def post(self, request):
#         music = request.data.get()
