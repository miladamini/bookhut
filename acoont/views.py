from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, rergisterForm, chekeOtpForm, AdderessForm
# Create your views here.
from random import randint
from uuid import uuid4
import ghasedakpack
from django.utils.crypto import get_random_string
from .models import otp, User

SMS = ghasedakpack.Ghasedak("acdb2b81aad8a24fc4a630c1622f4a848ab224ee53f5b5383cd19843bcdc87d7")


#
class User_Login(View):
    def get(self, request):
        ramz = request.GET.get('ramz')
        form = LoginForm()
        if ramz == 'True':
            milad = True

            return render(request, 'rejisteerUser.html', {'form': form, 'ramz': milad})
        else:
            milad = False

            return render(request, 'rejisteerUser.html', {'form': form, 'ramz': milad})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(phone=cd['phone']).exists() == True:
                us = User.objects.filter(phone=cd['phone']).first()
                if us.check_password(cd['password']) == True:
                    login(request, us)
                    return redirect('profView')
                else:
                    form.add_error('password', 'پسورد شما معتبر نیست')
            else:
                form.add_error('phone', 'شماره معتبری وارد کنید')
        else:
            form.add_error('phone', 'لطفا فرم را به درستی پر کنید')
        return render(request, 'rejisteerUser.html', {'form': form})


class registerViwe(View):
    def get(self, request):
        form = rergisterForm()
        return render(request, 'rejister.html', {'form': form})

    def post(self, request):
        form = rergisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randecode = randint(1000, 9999)

            us = User.objects.filter(phone=cd['phone']).exists()
            if us == False:
                token = str(uuid4())
                otp.objects.create(phone=cd['phone'], code=randecode, token=token)
                if cd['password'] != cd['password2']:
                    form.add_error('password', 'رمز ها باید مشابه به هم باشند')
                    return render(request, 'rejister.html', {'form': form})
                else:
                    SMS.verification(
                        {'receptor': cd['phone'], 'type': '1', 'template': 'jobinnet	', 'param1': randecode})
                    self.request.session['pass'] = {'password': cd['password'], 'name': cd['name']}
                    return redirect(reverse('acoont:check_otp') + f'?token={token}')
            else:
                form.add_error('phone', 'با این شماره قبلا ثبت نام شده است')
                return render(request, 'rejister.html', {'form': form})

        else:
            form.add_error('phone', 'فرم را به درستی پر کنید')
            return render(request, 'rejister.html', {'form': form})


class checkotpViwe(View):
    def get(self, request):
        form = chekeOtpForm()
        return render(request, 'check_otp.html', {'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = chekeOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if otp.objects.filter(code=cd['code'], token=token).exists():
                Otp = otp.objects.get(token=token)

                if self.request.session.get('pass') != None:
                    user = User.objects.create_user(phone=Otp.phone, password=request.session['pass']['password'])
                    login(request, user)
                    # del request.session['pass']
                    Otp.delete()
                    return redirect('profView')
                else:
                    user = User.objects.filter(phone=request.user.phone).first()
                    user.phone = request.session['phone']
                    user.save()
                    # login(request, user)
                    # del request.session['phone']
                    Otp.delete()
                    return redirect('profView')
            else:
                form.add_error('code', 'کد تایید اشتباه است')



        else:
            form.add_error('code', 'کد تایید اشتباه است')

        return render(request, 'check_otp.html', {'form': form})


#
# class AddAddress(View):
#     def post(self, request):
#         form = AdderessForm(request.POST)
#         if form.is_valid():
#             address = form.save(commit=False)
#             address.user = request.user
#             address.save()
#         return render(request, "add_address.html", {'form': form})
#
#     def get(self, request):
#         form = AdderessForm()
#         return render(request, "add_address.html", {'form': form})
#

def logout_user(request):
    logout(request)
    return redirect('/')
