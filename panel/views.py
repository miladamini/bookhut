from django.shortcuts import render, redirect
from django.views import View
from post.models import post, Podcast
from acoont.models import User
from django.db.models import Sum
from eshtrak.models import Day1, buy


# Create your views here.


class PanelView(View):
    def get(self, request):
        us = User.objects.count()
        blok = User.objects.filter(blok=True).count()
        vi = post.objects.aggregate(Sum('view'))['view__sum']
        rom = post.objects.all().count()
        P_vi = Podcast.objects.aggregate(Sum('view'))['view__sum']
        pod = Podcast.objects.all().count()
        roman_name = post.objects.all()
        esh = Day1.objects.all().count()
        bu = buy.objects.all().count()

        if request.user.is_authenticated:
            if request.user.is_admin == True:
                return render(request, 'panel.html',
                              {'user': us, 'blok': blok, 'vi': vi, 'rom': rom, 'P_vi': P_vi, 'pod': pod, 'esh': esh,
                               'buy': bu,
                               'roman_name': roman_name})
            else:
                return redirect(request.path_info)
        else:
            return redirect('acoont:register')
