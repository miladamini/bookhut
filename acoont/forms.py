from django import forms
from django.core import validators
from .models import UserAddress


def phon_number(vleu):
    if vleu[0] != '0':
        raise forms.ValidationError('شماره شما باید با عدد 0 شروع شود')


class LoginForm(forms.Form):
    phone = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})),
                            validators=[validators.MaxLengthValidator(11), validators.MinLengthValidator(11),
                                        phon_number])
    password = forms.CharField(widget=(forms.PasswordInput(attrs={'class': 'form-control'})))


class AdderessForm(forms.ModelForm):
    user = forms.ImageField(required=False)

    class Meta:
        model = UserAddress
        fields = '__all__'


class rergisterForm(forms.Form):
    name = forms.CharField(
        widget=(forms.TextInput(attrs={'class': 'form-control', 'id': 'signup-name', 'placeholder': 'نام کاربری'})))
    phone = forms.CharField(
        widget=(forms.TextInput(attrs={'class': 'form-control ', 'id': 'signup-phone', 'placeholder': 'شماره تلفن'})),
        validators=[validators.MaxLengthValidator(11), validators.MinLengthValidator(11),
                    phon_number])
    password = forms.CharField(widget=(
        forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'id': 'signup-password', 'placeholder': 'رمز عبور',
                   'minlength': '8'})))
    password2 = forms.CharField(widget=(forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'id': 'signup-password-confirm', 'placeholder': 'تایید رمز عبور',
               'minlength': '8'})))


class chekeOtpForm(forms.Form):
    code = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})),
                           validators=[validators.MaxLengthValidator(4), validators.MinLengthValidator(4)])
