import random
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from acoont.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import profForm, profFormusername, FormPhone, profFormimg, passwordForm, mediaForm, ResetpassForm
from django.shortcuts import redirect, reverse
from acoont.models import otp
# from random import random
from uuid import uuid4
import ghasedakpack

SMS = ghasedakpack.Ghasedak("acdb2b81aad8a24fc4a630c1622f4a848ab224ee53f5b5383cd19843bcdc87d7")
SMS2 = ghasedakpack.Ghasedak("9e7ef431bbe07d7f2b28cd88ca30b3458e2443e4e9a6254cb998e9bbe5c815ff")


# Create your views here.

class profView(View):
    def get(self, request):
        password = passwordForm()
        form1 = profForm()
        formUsername = profFormusername()
        profFormPhone = FormPhone()
        imgprof = profFormimg()
        link = mediaForm()
        return render(request, 'job-board-account-profile.html',
                      {'form1': form1, 'formUsername': formUsername, 'profFormPhone': profFormPhone,
                       'imgprof': imgprof, 'password': password, 'link': link})

    def post(self, request):
        link = mediaForm(request.POST)
        password = passwordForm(request.POST)
        imgprof = profFormimg(request.POST, files=request.FILES)
        token = request.GET.get('token')
        form1 = profForm(request.POST)
        profFormPhone = FormPhone(request.POST)
        formUsername = profFormusername(request.POST)
        if request.POST.get('email1') == 'email1':
            if form1.is_valid():
                cd = form1.cleaned_data
                us = User.objects.filter(phone=request.user.phone).first()
                us.email = cd['email']
                us.save()
                return redirect(request.path_info)
            else:
                form1.add_error('email', 'لطفا ایمیل معتبری وارد کنید')
        if request.POST.get('password1') == 'password1':
            if password.is_valid():
                cd = password.cleaned_data
                us = User.objects.filter(phone=request.user.phone).first()

                if cd['old_password'] != '':
                    us.check_password(cd['old_password'])
                    if us.check_password(cd['old_password']) != True:
                        password.add_error('old_password', 'رمز عبور فعلی شما اشتباه است لطفا دوباره تلاش کنید')
                    elif cd['new_password1'] != cd['new_password2']:
                        password.add_error('new_password1', 'رمز های عبور باید مانند هم باشند . لطفا دوباره تلاش کنید')
                    else:
                        us.set_password(cd['new_password1'])
                        us.save()
                        login(request, us)
                        return redirect(request.path_info)
            else:
                password.add_error('new_password1', 'رمز ها را به درست وارد کنید')

        if request.POST.get('img1') == 'img1':
            if imgprof.is_valid():
                cd = imgprof.cleaned_data
                us = User.objects.filter(phone=request.user.phone).first()
                us.img = cd['img']
                us.save()
                return redirect(request.path_info)
            else:
                imgprof.add_error('img', 'لطفا فایل معتبری وارد کنید')
        if request.POST.get('usernamein') == 'usernamein':
            if formUsername.is_valid():
                cd = formUsername.cleaned_data
                us = User.objects.filter(phone=request.user.phone).first()
                us.username = cd['username']
                us.save()
                return redirect(request.path_info)
            else:
                formUsername.add_error('username', 'نام کاربری را درست وارد کنید')

        if request.POST.get('link1') == 'link1':
            if link.is_valid():
                cd = link.cleaned_data
                us = User.objects.filter(phone=request.user.phone).first()
                us.facebook = cd['facebook']
                us.airbnb = cd['airbnb']
                us.twitter = cd['twitter']
                us.instagram = cd['instagram']
                us.save()
                return redirect(request.path_info)

        # if profFormPhone.is_valid():
        #     cd = profFormPhone.cleaned_data
        #     ph = User.objects.filter(phone=cd['phone']).exists()
        #
        #     if ph == True:
        #         profFormPhone.add_error('phone', 'با این شماره قبلا ثبت نام شده است')
        #     else:
        #
        #         randecode = randint(1000, 9999)
        #         print(randecode)
        #
        #         # SMS.verification({'receptor': cd['phone'], 'type': '1', 'template': 'jobinnet	', 'param1': randecode})
        #         token = str(uuid4())
        #         otp.objects.create(phone=cd['phone'], code=randecode, token=token)
        #
        #         self.request.session['phone'] = cd['phone']
        #
        #         return redirect(reverse('acoont:check_otp') + f'?token={token}')
        #
        # else:
        #     profFormPhone.add_error('phone', 'با این شماره قبلا ثبت نام شده است')

        return render(request, 'job-board-account-profile.html',
                      {'form1': form1, 'formUsername': formUsername, 'profFormPhone': profFormPhone,
                       'imgprof': imgprof, 'password': password, 'link': link})


class Passwordreset(View):
    def get(self, request):
        form = ResetpassForm()
        return render(request, 'resetpass.html', {'form': form})

    def post(self, request):
        form = ResetpassForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.filter(phone=cd['phone']).exists()
            if user == True:

                ramz = ''.join(
                    (random.choice('abcdxy1241m12m3m1lkn1243lk12knlk123nlknl1k23nlkn1lk2n3zpqr') for i in range(15)))
                us = User.objects.filter(phone=cd['phone']).first()
                us.set_password(ramz)
                us.save()

                SMS2.verification(
                    {'receptor': us.phone, 'type': '1', 'template': 'ramz', 'param1': ramz})

                return redirect(reverse('acoont:login') + f'?ramz=True')

            else:
                form.add_error('phone', 'هیچ حساب کاربری با این شماره وجود ندارد لطفا ثبت نام کنید')
                return render(request, 'resetpass.html', {'form': form})
