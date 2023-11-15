from django import forms
from django.core import validators

from . import models


class CommentsForm(forms.ModelForm):
    user = forms.ImageField()
    class Meta:
        model = models.Comments_post
        fields = '__all__'

