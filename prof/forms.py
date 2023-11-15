from django import forms
from django.forms import ModelForm

from acoont.models import User
from django.core import validators
from django.contrib.auth.forms import PasswordChangeForm

from django.core.exceptions import ValidationError


def phon_number(vleu):
    if vleu[0] != '0':
        raise forms.ValidationError('شماره شما باید با عدد 0 شروع شود')


class profForm(forms.Form):
    email = forms.EmailField(required=False,
                             widget=(forms.TextInput(
                                 attrs={'class': 'form-control mt-3', 'placeholder': 'ایمیل خود را وارد کنید'})), )


class profFormusername(forms.Form):
    username = forms.CharField(required=False,
                               widget=(forms.TextInput(attrs={'class': 'form-control mt-3',
                                                              'placeholder': 'نام کاربری خود را وارد کنید'})), )


class profFormimg(ModelForm):
    class Meta:
        model = User
        fields = ['img']


# class profFormimg(forms.Form):
#     img = forms.ImageField(required=False)


class FormPhone(forms.Form):
    phone = forms.CharField(required=False, widget=(forms.TextInput(attrs={'class': 'form-control'})),
                            validators=[validators.MaxLengthValidator(11), validators.MinLengthValidator(11),
                                        phon_number])


class passwordForm(forms.Form):
    old_password = forms.CharField(required=False,
                                   widget=(forms.PasswordInput(
                                       attrs={'class': 'form-control', 'id': 'account-password-current',
                                              'placeholder': 'رمز عبور فعلی را وارد کنید'})))
    new_password1 = forms.CharField(required=False,
                                    widget=(forms.PasswordInput(
                                        attrs={'class': 'form-control', 'id': 'account-password-new',
                                               'placeholder': 'رمز عبور جدید را وارد کنید'})))
    new_password2 = forms.CharField(required=False,
                                    widget=(forms.PasswordInput(
                                        attrs={'class': 'form-control', 'id': 'account-password-confirm',
                                               'placeholder': 'رمز عبور جدید را مجدد وارد کنید'})))


class mediaForm(forms.Form):
    facebook = forms.URLField(required=False,
                              widget=forms.URLInput(
                                  attrs={'class': 'form-control', 'placeholder': 'اکانت فیسبوک خود را وارد کنید'}))
    airbnb = forms.URLField(required=False,
                            widget=forms.URLInput(
                                attrs={'class': 'form-control', 'placeholder': 'سایر اکانت های خود را وارد کنید'}))
    twitter = forms.URLField(required=False,
                             widget=forms.URLInput(
                                 attrs={'class': 'form-control', 'placeholder': 'اکانت توییتر خود را وارد کنید'}))
    instagram = forms.URLField(required=False,
                               widget=forms.URLInput(
                                   attrs={'class': 'form-control', 'placeholder': 'اکانت اینستاگرام خود را وارد کنید'}))


class ResetpassForm(forms.Form):
    phone = forms.CharField(
        widget=(forms.TextInput(attrs={'class': 'form-control ', 'id': 'signup-phone', 'placeholder': 'شماره تلفن'})),
        validators=[validators.MaxLengthValidator(11), validators.MinLengthValidator(11),
                    phon_number])
