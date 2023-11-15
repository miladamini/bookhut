from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

from admin_interface.models import Theme
from .forms import hmkariForm, AutherromanForm
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from post.models import post, Podcast
from .models import Advertise, Hmtext, Autherroman, Competition, UserJvayez, Questions
from django.views.generic import TemplateView
from eshtrak.models import Day1, ssion, buy
from acoont.models import User
from django.utils import timezone


# Create your views here.
class HomeView(View):
    def get(self, request):
        Post = post.objects.filter(Accepted=True).all()
        if request.user.is_authenticated:
            Buy = buy.objects.filter(user=request.user).exists()
        else:
            Buy = None

        pad = Podcast.objects.filter(Accepted=True).all()
        Post2 = post.objects.filter(created__lte=timezone.now(), Accepted=True).reverse()[:3]
        pad2 = Podcast.objects.filter(created__lte=timezone.now(), Accepted=True).reverse()[:3]
        Post3 = post.objects.order_by('created').filter(Accepted=True).all()[:3]
        Post4 = post.objects.filter(Accepted=True).all().reverse()[:6]

        Category1 = Podcast.objects.filter(Accepted=True, correction=1).all().exists()
        if Category1 == False:
            Category1 = None
        else:
            Category1 = Podcast.objects.filter(Accepted=True, correction=1).reverse()[:5]
        ###########################################################################
        Category2 = Podcast.objects.filter(Accepted=True, correction=2).all().exists()
        if Category2 == False:
            Category2 = None
        else:
            Category2 = Podcast.objects.filter(Accepted=True, correction=2).reverse()[:5]
        ###############################################################################
        Category3 = Podcast.objects.filter(Accepted=True, correction=3).all().exists()
        if Category3 == False:
            Category3 = None
        else:
            Category3 = Podcast.objects.filter(Accepted=True, correction=3).reverse()[:5]
        ##########################################################################
        zanr1 = post.objects.filter(Accepted=True, correction=1).all().exists()
        if zanr1 == False:
            zanr1 = None
        else:
            zanr1 = post.objects.filter(Accepted=True, correction=1).all().reverse()[:5]
        # 11111111111111111111111111111
        zanr2 = post.objects.filter(Accepted=True, correction=2).all().exists()
        if zanr2 == False:
            zanr2 = None
        else:
            zanr2 = post.objects.filter(Accepted=True, correction=2).all().reverse()[:5]
        ##33333333333333333333333333333333
        zanr3 = post.objects.filter(Accepted=True, correction=3).all().exists()
        if zanr3 == False:
            zanr3 = None
        else:
            zanr3 = post.objects.filter(Accepted=True, correction=3).all().reverse()[:5]
        # 44444444444444444444444444444444444444
        zanr4 = post.objects.filter(Accepted=True, correction=4).all().exists()
        if zanr4 == False:
            zanr4 = None
        else:
            zanr4 = post.objects.filter(Accepted=True, correction=4).all().reverse()[:5]
        # 55555555555555555555555555
        zanr5 = post.objects.filter(Accepted=True, correction=5).all().exists()
        if zanr5 == False:
            zanr5 = None
        else:
            zanr5 = post.objects.filter(Accepted=True, correction=5).all().reverse()[:5]
        # 66666666666666666666666
        zanr6 = post.objects.filter(Accepted=True, correction=6).all().exists()
        if zanr6 == False:
            zanr6 = None
        else:
            zanr6 = post.objects.filter(Accepted=True, correction=6).all().reverse()[:5]
        # 7777777777777777777777777
        zanr7 = post.objects.filter(Accepted=True, correction=7).all().exists()
        if zanr7 == False:
            zanr7 = None
        else:
            zanr7 = post.objects.filter(Accepted=True, correction=7).all().reverse()[:5]
        # 88888888888888888
        zanr8 = post.objects.filter(Accepted=True, correction=8).all().exists()
        if zanr8 == False:
            zanr8 = None
        else:
            zanr8 = post.objects.filter(Accepted=True, correction=8).all().reverse()[:5]

        tab = Advertise.objects.filter(id_fild=1).all()

        if request.user.is_authenticated:
            mi = Day1.objects.filter(user=request.user).first()
            milad = Day1.objects.filter(user=request.user).first()
            mi1 = Day1.objects.filter(user=request.user).exists()
            userr = User.objects.filter(phone=request.user.phone).first()
            if Day1.objects.count() != 0:
                if mi1 == True:
                    if mi.user == request.user:
                        if timezone.datetime.timestamp(milad.time) >= timezone.datetime.timestamp(timezone.now()):
                            userr.eshtrak = True
                            userr.save()
                        else:
                            userr.eshtrak = False
                            userr.save()
                            milad.delete()
        return render(request, 'index.html',
                      {'post': Post, 'post4': Post4, 'pad': pad, 'post2': Post2, 'pad2': pad2, 'post3': Post3,
                       'tab': tab, 'zanr1': zanr1, 'zanr2': zanr2, 'zanr3': zanr3, 'zanr4': zanr4, 'zanr5': zanr5,
                       'zanr6': zanr6, 'zanr7': zanr7, 'zanr8': zanr8, 'cat1': Category1, 'cat2': Category2,
                       'cat3': Category3, 'Buy': Buy})


class Category1View(View):
    def get(self, request):
        Correction = Podcast.objects.filter(Accepted=True, correction=1).all()
        page_number = request.GET.get('page')
        page = Paginator(Correction, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan': object_list})


class Category2View(View):
    def get(self, request):
        Correction = Podcast.objects.filter(Accepted=True, correction=2).all()
        page_number = request.GET.get('page')
        page = Paginator(Correction, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan': object_list})


class Category3View(View):
    def get(self, request):
        Correction = Podcast.objects.filter(Accepted=True, correction=3).all()
        page_number = request.GET.get('page')
        page = Paginator(Correction, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan': object_list})


class CorrectionView1(View):
    def get(self, request):
        zanr1 = post.objects.filter(Accepted=True, correction=1).all()
        page_number = request.GET.get('page')
        page = Paginator(zanr1, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan1': object_list})


class CorrectionView2(View):
    def get(self, request):
        zanr2 = post.objects.filter(Accepted=True, correction=2).all()
        page_number = request.GET.get('page')
        page = Paginator(zanr2, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan1': object_list})


class CorrectionView3(View):
    def get(self, request):
        zanr3 = post.objects.filter(Accepted=True, correction=3).all()
        page_number = request.GET.get('page')
        page = Paginator(zanr3, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan1': object_list})


class CorrectionView4(View):
    def get(self, request):
        zanr4 = post.objects.filter(Accepted=True, correction=4).all()
        page_number = request.GET.get('page')
        page = Paginator(zanr4, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan1': object_list})


class CorrectionView5(View):
    def get(self, request):
        zanr5 = post.objects.filter(Accepted=True, correction=5).all()
        page_number = request.GET.get('page')
        page = Paginator(zanr5, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan1': object_list})


class CorrectionView6(View):
    def get(self, request):
        zanr6 = post.objects.filter(Accepted=True, correction=6).all()
        page_number = request.GET.get('page')
        page = Paginator(zanr6, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan1': object_list})


class CorrectionView7(View):
    def get(self, request):
        zanr7 = post.objects.filter(Accepted=True, correction=7).all()
        page_number = request.GET.get('page')
        page = Paginator(zanr7, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan1': object_list})


class CorrectionView8(View):
    def get(self, request):
        zanr8 = post.objects.filter(Accepted=True, correction=8).all()
        page_number = request.GET.get('page')
        page = Paginator(zanr8, 3)
        object_list = page.get_page(page_number)
        return render(request, 'Correction.html', {'zan1': object_list})


class hamkati(View):
    def get(self, request):
        form = hmkariForm()
        return render(request, 'hamkarl.html', {'form': form})

    def post(self, request):
        form = hmkariForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Hmtext.objects.create(user=request.user, name=cd['name'], text=cd['text'], file=cd['file'])
            return redirect(request.path_info)
        else:
            form.add_error('name', 'لطفا همه قسمت هارا به درستی پر کنید')
            return render(request, 'hamkarl.html', {'form': form})


class AutherromanView(View):
    def get(self, request):
        form = AutherromanForm()
        if request.user.is_authenticated:
            return render(request, 'Autherroman.html', {'form': form})
        else:
            return redirect('acoont:login')

    def post(self, request):
        form = AutherromanForm(request.POST, files=request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            Autherroman.objects.create(user=request.user, name=cd['name'], text=cd['text'], file=cd['file'])
            return redirect(request.path_info)
        else:
            form.add_error('user', 'لطفا همه قسمت هارا به درستی پر کنید')
            return render(request, 'Autherroman.html', {'form': form})


class Robot(TemplateView):
    template_name = 'Robots.txt'
    content_type = 'text/plain'


class Serch(View):
    def get(self, request):
        if request.user.is_authenticated:
            mi = Day1.objects.filter(user=request.user).first()
            milad = Day1.objects.filter(user=request.user).first()
            mi1 = Day1.objects.filter(user=request.user).exists()
            userr = User.objects.filter(phone=request.user.phone).first()
            if Day1.objects.count() != 0:
                if mi1 == True:
                    if mi.user == request.user:
                        if timezone.datetime.timestamp(milad.time) >= timezone.datetime.timestamp(timezone.now()):
                            userr.eshtrak = True
                            userr.save()
                        else:
                            userr.eshtrak = False
                            userr.save()
                            milad.delete()
        q = request.GET.get('q')
        serch = post.objects.filter(title__icontains=q)
        pd_serck = Podcast.objects.filter(title__icontains=q)

        return render(request, 'serch.html', {'sh': serch, 'pd': pd_serck})


class NotPdf(View):
    def get(self, request):

        if request.user.is_authenticated:
            mi = Day1.objects.filter(user=request.user).first()
            milad = Day1.objects.filter(user=request.user).first()
            mi1 = Day1.objects.filter(user=request.user).exists()
            userr = User.objects.filter(phone=request.user.phone).first()
            if Day1.objects.count() != 0:
                if mi1 == True:
                    if mi.user == request.user:
                        if timezone.datetime.timestamp(milad.time) >= timezone.datetime.timestamp(timezone.now()):
                            userr.eshtrak = True
                            userr.save()
                        else:
                            userr.eshtrak = False
                            userr.save()
                            milad.delete()
        return render(request, 'notPDF.html')


class esh(View):
    def get(self, request):
        if 'amini' in self.request.session:
            del self.request.session['amini']
            del self.request.session['milad']
            del self.request.session['discode']
        tab = Advertise.objects.all()
        milad1 = Day1.objects.filter(user=request.user).first()

        if request.user.is_authenticated:
            mi = Day1.objects.filter(user=request.user).first()
            milad = Day1.objects.filter(user=request.user).first()
            mi1 = Day1.objects.filter(user=request.user).exists()
            userr = User.objects.filter(phone=request.user.phone).first()
            if Day1.objects.count() != 0:
                if mi1 == True:
                    if mi.user == request.user:
                        if timezone.datetime.timestamp(milad.time) >= timezone.datetime.timestamp(timezone.now()):
                            userr.eshtrak = True
                            userr.save()
                        else:
                            userr.eshtrak = False
                            userr.save()
                            milad.delete()
                        milad.delete()
        return render(request, 'eshtrak.html', {'mi': milad1, 'tab': tab})


class profile(View):
    def get(self, request):
        milad1 = Day1.objects.filter(user=request.user).first()
        Buy = buy.objects.filter(user=request.user).all()
        if request.user.is_authenticated:
            mi = Day1.objects.filter(user=request.user).first()
            milad = Day1.objects.filter(user=request.user).first()
            mi1 = Day1.objects.filter(user=request.user).exists()
            userr = User.objects.filter(phone=request.user.phone).first()
            if Day1.objects.count() != 0:
                if mi1 == True:
                    if mi.user == request.user:
                        if timezone.datetime.timestamp(milad.time) >= timezone.datetime.timestamp(timezone.now()):
                            userr.eshtrak = True
                            userr.save()
                        else:
                            userr.eshtrak = False
                            userr.save()
                            milad.delete()

        return render(request, 'profile.html', {'mi': milad1, 'Buy': Buy})


class CompetitionView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            Buy = buy.objects.filter(user=request.user, roman_id=id).exists()
            usJvayez = UserJvayez.objects.filter(user=request.user, roman_id=id).exists()
            soalat = Questions.objects.filter(roman_id=id).first()
            if request.user.eshtrak == True or Buy == True:
                if usJvayez == False:
                    UserJvayez.objects.create(user=request.user, roman_id=id, Condition=True)

                return render(request, 'jvayez.html', {'soalat': soalat})
            else:
                return render(request, 'Not_jvayez.html')
        else:
            return redirect('/register')

    def post(self, request):
        user = request.user
        roman = request.POST.get('roman')
        text = request.POST.get('text')
        Competition.objects.create(user=user, roman=roman, text=text)
        return redirect('/')


class My_chat(View):
    def get(self, request):
        return render(request, 'my_chat.html')


from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client

MERCHANT = '5878c037-ada9-4c7c-8231-8d76aff222ea'
email = ''
# from .tasks import payment_completed

client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# mobile = '09123456789'  # Optional
CallbackURL = 'http://127.0.0.1:8000/verify'  # Important: need to edit for realy server.


class send_req(View):
    def get(self, request):
        if self.request.session.get('discode') != None:
            code = request.session['discode']['kaymat']
        else:
            code = self.request.session['discode1']['kaymat']

        us = User.objects.filter(phone=request.user).first()
        mobile = us.phone
        amount = code  # Toman / Required
        if self.request.session.get('discode') != None:
            ssion.objects.create(user=request.user,
                                 kaymat=request.session['discode']['kaymat'],
                                 modate=request.session['discode']['modate'],
                                 time=request.session['discode']['tiem']),


        else:
            ssion.objects.create(user=request.user,
                                 kaymat=request.session['discode1']['kaymat'],
                                 modate=request.session['discode1']['modate'],
                                 time=request.session['discode1']['tiem'])
        self.request.session['code'] = int(code)

        result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))


class verify(View):
    def get(self, request):
        user = ssion.objects.filter(user=request.user).first()
        if request.GET.get('Status') == 'OK':
            mi = self.request.session['code']
            amount = mi
            result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
            if result.Status == 100:
                Day1.objects.create(user=user.user, kaymat=user.kaymat, modate=user.modate,
                                    time=user.time)
                if self.request.session.get('discode') != None:
                    del self.request.session['discode']
                if self.request.session.get('amini') != None:
                    del self.request.session['amini']
                if self.request.session.get('discode1') != None:
                    del self.request.session['discode1']
                if user != None:
                    user.delete()
                del self.request.session['code']
                return render(request, "success.html", {"id": result.RefID})
            elif result.Status == 101:
                del self.request.session['code']
                if self.request.session.get('discode') != None:
                    del self.request.session['discode']
                if self.request.session.get('amini') != None:
                    del self.request.session['amini']
                if self.request.session.get('discode1') != None:
                    del self.request.session['discode1']
                if user != None:
                    user.delete()
                return render(request, "submited.html", {"status": result.Status})
            else:
                del self.request.session['code']
                if self.request.session.get('discode') != None:
                    del self.request.session['discode']
                if self.request.session.get('amini') != None:
                    del self.request.session['amini']
                if self.request.session.get('discode1') != None:
                    del self.request.session['discode1']
                if user != None:
                    user.delete()
                return render(request, "failed.html", {"status": result.Status})
        else:
            del self.request.session['code']
            if self.request.session.get('discode') != None:
                del self.request.session['discode']
            if self.request.session.get('amini') != None:
                del self.request.session['amini']
            if self.request.session.get('discode1') != None:
                del self.request.session['discode1']
            if user != None:
                user.delete()

            return render(request, "cancel.html")

# email = ''
# MERCHANT = 'cdc3ce39-524c-4869-aabc-7af4a39b7705'
# # from .tasks import payment_completed
# client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# description = "وبسایت آکورمان"  # Required
# # mobile = '09123456789'  # Optional
# CallbackURL = 'https://akoroman.ir/verifyboy'  # Important: need to edit for realy server.


# class send_req2(View):
#     def get(self, request):
#         us = User.objects.filter(phone=request.user).first()
#         mobile = us.phone
#         amount = self.request.session['eshtrak']['many']
#         result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
#         if result.Status == 100:
#             return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
#         else:
#             return HttpResponse('Error code: ' + str(result.Status))


# class verify2(View):
#     def get(self, request):
#         user = ssion.objects.filter(user=request.user).first()
#         if request.GET.get('Status') == 'OK':
#             amount =  self.request.session['eshtrak']['many']
#             result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
#             if result.Status == 100:
#                 us = User.objects.filter(phone=request.user).first()
#                 buy.objects.create(user=us,roman_id=self.request.session['eshtrak']['title'],many=self.request.session['eshtrak']['many'])
#                 return render(request, "success.html", {"id": result.RefID})
#             elif result.Status == 101:

#                 return render(request, "submited.html", {"status": result.Status})
#             else:

#                 return render(request, "failed.html", {"status": result.Status})
#         else:
#             return render(request, "cancel.html")
