from post import models
from rest_framework import serializers


class PostSer(serializers.ModelSerializer):
    class Meta:
        models = models.post
        fields = '__all__'

    # برای اعتبار سنجی های تک فیلدی
    # def validate_author(self, value):
    #     return value

    # برای اعتبار سنجی دست جمعی یا ابجکت لول
    # def validate(self, attrs):
    #     if attrs['author'] == 'milad':
    #         raise serializers.ValidationError('این یک ارور ازمایشی هست')
    #     return attrs
    #


class PadcastrSer(serializers.ModelSerializer):
    class Meta:
        models = models.Podcast
        fields = '__all__'


class CoomentPostSer(serializers.ModelSerializer):
    class Meta:
        models = models.Comments_post
        fields = '__all__'


class CoomentPadcastSer(serializers.ModelSerializer):
    class Meta:
        models = models.Comments_Podcast
        fields = '__all__'


class TamsSer(serializers.ModelSerializer):
    class Meta:
        models = models.Tamas_ba_ma
        fields = '__all__'


class PartRomanSer(serializers.ModelSerializer):
    class Meta:
        models = models.Part_roman
        fields = '__all__'


class PartPadcastSer(serializers.ModelSerializer):
    class Meta:
        models = models.Part_pad
        fields = '__all__'
