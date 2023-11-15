from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


# Create your views here.

class HomeViwe(APIView):
    def get(self, request):
        pass
