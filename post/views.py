import requests
from django.contrib.auth.models import Permission
from django.shortcuts import render, get_object_or_404, redirect
from .models import post, Podcast, Comments_Podcast, Tamas_ba_ma, Comments_post, Part_roman, Part_pad

from django.core.paginator import Paginator

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from post.models import post, Podcast
from home.models import Advertise, Hmtext, Autherroman, Competition, UserJvayez, abutsaznde, abutkarbar
from django.views.generic import TemplateView
from eshtrak.models import Day1, ssion, buy
from acoont.models import User, user_part
from django.utils import timezone


# Create your views here.

class PartView(View):
    def get(self, request, slug):
        Post = get_object_or_404(post, slug=slug, Accepted=True)
        rom = Part_roman.objects.order_by('a_id').filter(roman=Post)
        return render(request, 'open-book.html', {'rom': rom})


class RomanDitail(View):
    def get(self, request, slug):
        li = slug
        Post = get_object_or_404(post, slug=slug, Accepted=True)
        if Post.eshtrak == True:
            self.request.session['eshtrak'] = {'many': int(Post.buy_rom), 'title': int(Post.id)}
        if request.user.is_authenticated:
            Buy = buy.objects.filter(user=request.user, roman=Post).exists()
            Userjv = UserJvayez.objects.filter(user=request.user, roman=Post).exists()
        else:
            Buy = None
            Userjv = None
        rom = Part_roman.objects.order_by('a_id').filter(roman=Post)
        mi11 = Part_roman.objects.all().filter(roman=Post).last()
        po = Comments_post.objects.filter(articel=Post).count()
        po2 = Comments_post.objects.filter(articel=Post)
        Post.view += 1
        Post.save()
        tab = Advertise.objects.filter(id_fild=2).all()

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
        return render(request, 'ditaileroman.html',
                      {'post': Post, 'milad': mi11, 'rom': rom, 'po': po, 'po2': po2, 'tab': tab, 'Buy': Buy,
                       'Userjv': Userjv, 'li': li})

    def post(self, request, slug):
        Post = get_object_or_404(post.objects.filter(Accepted=True), slug=slug)
        text = request.POST.get('text')
        name = request.POST.get('name')
        parent = request.POST.get('parent')
        if request.user.is_admin == True:
            Comments_post.objects.create(articel=Post, user=request.user, name=name, parent_id=parent, text=text,
                                         user_admin=True)
        else:
            Comments_post.objects.create(articel=Post, user=request.user, name=name, parent_id=parent, text=text)

        return redirect(request.path_info)


class Post_ditail(View):
    def get(self, request, slug):
        Post = get_object_or_404(post, slug=slug, Accepted=True)
        if Post.eshtrak == True:
            self.request.session['eshtrak'] = {'many': int(Post.buy_rom), 'title': int(Post.id)}
        if request.user.is_authenticated:
            Buy = buy.objects.filter(user=request.user, roman=Post).exists()
            Userjv = UserJvayez.objects.filter(user=request.user, roman=Post).exists()
        else:
            Buy = None
            Userjv = None
        rom = Part_roman.objects.order_by('a_id').filter(roman=Post)
        mi11 = Part_roman.objects.all().filter(roman=Post).last()
        po = Comments_post.objects.filter(articel=Post).count()
        Post.view += 1
        Post.save()
        tab = Advertise.objects.filter(id_fild=2).all()

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
        return render(request, 'single.html',
                      {'post': Post, 'milad': mi11, 'rom': rom, 'po': po, 'tab': tab, 'Buy': Buy, 'Userjv': Userjv, })

    def post(self, request, slug):
        Post = get_object_or_404(post.objects.filter(Accepted=True), slug=slug)
        text = request.POST.get('text')
        name = request.POST.get('name')
        parent = request.POST.get('parent')
        Comments_post.objects.create(articel=Post, user=request.user, name=name, parent_id=parent, text=text)
        return redirect(request.path_info)


class Podcast_ditail(View):
    def get(self, request, slug):
        pod = get_object_or_404(Podcast.objects.filter(Accepted=True), slug=slug)
        music = Part_pad.objects.filter(pad=pod)
        po = Comments_Podcast.objects.filter(articel=pod).count()
        pad2 = Podcast.objects.filter(created__lte=timezone.now(), Accepted=True).reverse()[:3]
        padcst = Podcast.objects.filter(Accepted=True, slug=slug).first()
        padcst.view += 1
        padcst.save()
        tab = Advertise.objects.filter(id_fild=3).all()

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
        return render(request, 'si.html',
                      {'pod': pod, 'pod2': pad2, 'music': music, 'pod3': pod, 'po': po, 'podcast': padcst, 'tab': tab})

    def post(self, request, slug):
        pod = get_object_or_404(Podcast.objects.filter(Accepted=True), slug=slug)
        name = request.POST.get('name')
        text = request.POST.get('text')
        parent = request.POST.get('parent')
        Comments_Podcast.objects.create(articel=pod, user=request.user, name=name, parent_id=parent, text=text)
        return redirect(request.path_info)


class catgory_pad(View):
    def get(self, request):
        Post = Podcast.objects.filter(Accepted=True).all()
        page_number = request.GET.get('page')
        page = Paginator(Post, 3)
        object_list = page.get_page(page_number)
        if request.user.is_authenticated:
            mi = Day1.objects.all().first()
            milad = Day1.objects.filter(user=request.user).first()
            userr = User.objects.filter(phone=request.user.phone).first()
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
        return render(request, 'category_pad.html', {'post': object_list})


class catgory_roman(View):
    def get(self, request):
        Post = post.objects.filter(Accepted=True).all()
        page_number = request.GET.get('page')
        page = Paginator(Post, 3)
        object_list = page.get_page(page_number)
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
        return render(request, 'category.html', {'post': object_list})


class ContactView(View):
    def get(self, request):
        return render(request, 'page-blank.html')

    def post(self, request):
        name = request.POST.get('name')
        text = request.POST.get('text')
        Tamas_ba_ma.objects.create(user=request.user, text=text, name=name)
        return redirect('/')


class AbuteView(View):
    def get(self, request):
        malek = abutsaznde.objects.all().first()
        karbar = abutkarbar.objects.all()
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
        return render(request, 'blok.html', {'malek': malek, 'karbar': karbar})


class UserAdminView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.part == True:
                prat_post = post.objects.all()
                part_kole = Part_roman.objects.filter(user=request.user).count()
                user = user_part.objects.filter(user=request.user).exists()
                if user == False:
                    user_part.objects.create(user=request.user, kole_part=part_kole, bki_part=part_kole)
                user2 = user_part.objects.filter(user=request.user).first()
                user2.bki_part = user2.kole_part - user2.padakt_part
                user2.kole_part = part_kole
                user2.save()

                part = user_part.objects.filter(user=request.user).first()
                milad = Part_roman.objects.all()
                return render(request, 'part_roman.html', {'part': prat_post, 'user_part': part, 'milad': milad})
            else:
                return redirect('/')
        else:
            return redirect('register/')

    def post(self, request):
        roman = request.POST.get('roman')
        Post = post.objects.filter(title=roman).first()
        body = request.POST.get('body')
        hr = request.POST.get('hr')
        ad = request.POST.get('ad')
        Part_roman.objects.create(roman=Post, body=body, user=request.user, name=hr, a_id=ad)
        return redirect(request.path_info)


class PdfView(View):
    def get(self, request):
        qveri = Part_roman.objects.filter(Pdf=True).all()
        return render(request, 'PDFnew.html', {'q': qveri})




email = ''
MERCHANT = 'your MERCHANT code'
# from .tasks import payment_completed
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "وبسایت آکورمان"  # Required
# mobile = '09123456789'  # Optional
CallbackURL = 'https://akoroman.ir/verifyboy'  # Important: need to edit for realy server.


class send_req2(View):
    def get(self, request):
        us = User.objects.filter(phone=request.user).first()
        mobile = us.phone
        amount = self.request.session['eshtrak']['many']
        result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))


class verify2(View):
    def get(self, request):
        user = ssion.objects.filter(user=request.user).first()
        if request.GET.get('Status') == 'OK':
            amount = self.request.session['eshtrak']['many']
            result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
            if result.Status == 100:
                us = User.objects.filter(phone=request.user).first()
                buy.objects.create(user=us, roman_id=self.request.session['eshtrak']['title'],
                                   many=self.request.session['eshtrak']['many'])
                return render(request, "success.html", {"id": result.RefID})
            elif result.Status == 101:

                return render(request, "submited.html", {"status": result.Status})
            else:

                return render(request, "failed.html", {"status": result.Status})
        else:
            return render(request, "cancel.html")
