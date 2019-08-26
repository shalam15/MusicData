from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Authentication
from .serializers import AuthenticationSerializer

class AuthenticationView(viewsets.ModelViewSet):
    queryset = Authentication.objects.all()
    serializer_class = AuthenticationSerializer

