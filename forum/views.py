from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from acoont.models import User
from .models import UserChatModel, Chatemodel
from .serializers import Userser, Chatser, Chatuserser, Partser
from post.models import Part_roman


# Create your views here.

class DelView(APIView):
    def get(self, request, pk):
        model = UserChatModel.objects.filter(id=pk)
        model.delete()
        ser = Chatuserser(instance=model, many=True)
        return Response(ser.data)


class TextView(APIView):
    def get(self, request, pk):
        model = UserChatModel.objects.filter(id=pk)
        ser = Chatuserser(instance=model, many=True)
        return Response(ser.data)


class ChatView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            users = User.objects.filter(phone=request.user.phone).first()
            ser = Userser(instance=users)
            return Response(ser.data)
        else:
            return redirect('acoont:login')


class GapView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            users = Chatemodel.objects.all()
            ser = Chatser(instance=users, many=True)
            return Response(ser.data)
        else:
            return redirect('acoont:login')


class GapViewPost(APIView):
    def post(self, request):
        ser = Chatser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'True': True})
        return Response(Chatuserser.errors)


class UserChatView(APIView):
    def get(self, request, pk):
        if request.user.is_authenticated:
            users = UserChatModel.objects.filter(chat_m_id=pk)
            ser = Chatuserser(instance=users, many=True)
            return Response(ser.data)
        else:
            return redirect('acoont:login')


class UserChatViewPost(APIView):
    def post(self, request):
        ser = Chatuserser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'True': True})
        return Response(Chatuserser.errors)


class PartVeiw(APIView):
    def post(self, request):
        ser = Partser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'True': True})
        return Response(Partser.errors)


class PartGert(APIView):
    def get(self, request, pk):
        part = Part_roman.objects.filter(roman_id=pk).order_by('created_ad')[:1]
        ser = Partser(instance=part, many=True)
        return Response(ser.data)
