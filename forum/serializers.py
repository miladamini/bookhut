from rest_framework import serializers
from acoont.models import User
from .models import UserChatModel, Chatemodel
from post.models import Part_roman, post


class Userser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Partser(serializers.ModelSerializer):
    class Meta:
        model = Part_roman
        exclude = ['Pdf']

        # fields = '__all__'


class Postser(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'


class Chatser(serializers.ModelSerializer):
    class Meta:
        model = Chatemodel
        fields = '__all__'


class Chatuserser(serializers.ModelSerializer):
    class Meta:
        model = UserChatModel
        fields = '__all__'
