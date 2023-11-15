from django import forms
from .models import Hmtext
from django.core import validators

def phon_number(vleu):
    if vleu[0] != '0':
        raise forms.ValidationError('شماره شما باید با عدد 0 شروع شود')
class hmkariForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                           validators=[validators.MaxLengthValidator(100)], label='اسم شما')
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='توضیحات')
    file = forms.FileField(validators=[validators.FileExtensionValidator], required=False)


class AutherromanForm(forms.Form):
    user = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})),
                           validators=[validators.MaxLengthValidator(11), validators.MinLengthValidator(11),
                                       phon_number])
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),
                           validators=[validators.MaxLengthValidator(100)], label='اسم شما')
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='توضیحات')
    file = forms.FileField(validators=[validators.FileExtensionValidator], required=False)