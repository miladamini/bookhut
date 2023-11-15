from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from acoont.models import User
from .models import tkfifcode, Day1, buy
from post.models import post
from django.contrib import messages


class eshtrakDay(View):
    def get(self, request):

        timedel = timezone.datetime.now() + timezone.timedelta(days=1)
        self.request.session['discode1'] = {'user': str(request.user), 'kaymat': int(5000), 'modate': 'یک روزه',
                                            'tiem': str(timedel)}

        self.request.session['milad'] = 5000
        order1 = 'یک روزه 5 هزار '
        order = self.request.session.get('amini', 5000)
        self.request.session.save()
        return render(request, 'eshtrak7.html', {'or': order, 'or2': order1})

    def post(self, request):
        timedel = timezone.datetime.now() + timezone.timedelta(days=1)
        code_t = self.request.session['milad']
        code = request.POST.get('code')
        t_code = tkfifcode.objects.all().first()
        if code == str(t_code):
            dis = get_object_or_404(tkfifcode, name=code)
            code_t -= code_t * dis.darsad / 100
            dis.tedad -= 1
            dis.save()
            self.request.session['discode'] = {'user': str(request.user), 'kaymat': int(code_t), 'modate': 'یک روزه',
                                               'tiem': str(timedel)}
            self.request.session['amini'] = int(code_t)
            self.request.session.modified = True
            return redirect(request.path_info)
        else:
            mimi = tkfifcode.objects.first()
            erroe = True
            self.request.session['milad'] = 5000
            order1 = 'یک روزه 5 هزار'
            order = self.request.session.get('amini', 5000)
            self.request.session.save()
            return render(request, 'eshtrak7.html', {'or': order, 'or2': order1, 'mimi': mimi, 'er': erroe})


class eshtrakWeek(View):
    def get(self, request):

        timedel = timezone.datetime.now() + timezone.timedelta(days=7)
        self.request.session['discode1'] = {'user': str(request.user), 'kaymat': int(30000), 'modate': 'یک هفته',
                                            'tiem': str(timedel)}

        self.request.session['milad'] = 30000
        order1 = 'یک هفته 30 هزار'
        order = self.request.session.get('amini', 30000)
        self.request.session.save()
        return render(request, 'eshtrak7.html', {'or': order, 'or2': order1})

    def post(self, request):
        timedel = timezone.datetime.now() + timezone.timedelta(days=7)
        code_t = self.request.session['milad']
        code = request.POST.get('code')
        t_code = tkfifcode.objects.all().first()
        if code == str(t_code):
            dis = get_object_or_404(tkfifcode, name=code)
            code_t -= code_t * dis.darsad / 100
            dis.tedad -= 1
            dis.save()
            self.request.session['discode'] = {'user': str(request.user), 'kaymat': int(code_t), 'modate': 'یک هفته',
                                               'tiem': str(timedel)}
            self.request.session['amini'] = int(code_t)
            self.request.session.modified = True
            return redirect(request.path_info)
        else:
            mimi = tkfifcode.objects.first()
            erroe = True
            self.request.session['milad'] = 30000
            order1 = 'یک هفته 30 هزار'
            order = self.request.session.get('amini', 30000)
            self.request.session.save()
            return render(request, 'eshtrak7.html', {'or': order, 'or2': order1, 'mimi': mimi, 'er': erroe})


class eshtrakMonth(View):
    def get(self, request):

        timedel = timezone.datetime.now() + timezone.timedelta(days=30)
        self.request.session['discode1'] = {'user': str(request.user), 'kaymat': int(100000), 'modate': 'یک ماهه',
                                            'tiem': str(timedel)}

        self.request.session['milad'] = 100000
        order1 = 'یک ماهه 100 هزار'
        order = self.request.session.get('amini', 100000)
        self.request.session.save()
        return render(request, 'eshtrak7.html', {'or': order, 'or2': order1})

    def post(self, request):
        timedel = timezone.datetime.now() + timezone.timedelta(days=30)
        code_t = self.request.session['milad']
        code = request.POST.get('code')
        t_code = tkfifcode.objects.all().first()
        if code == str(t_code):
            dis = get_object_or_404(tkfifcode, name=code)
            code_t -= code_t * dis.darsad / 100
            dis.tedad -= 1
            dis.save()
            self.request.session['discode'] = {'user': str(request.user), 'kaymat': int(code_t), 'modate': 'یک ماهه',
                                               'tiem': str(timedel)}
            self.request.session['amini'] = int(code_t)
            self.request.session.modified = True
            return redirect(request.path_info)
        else:
            mimi = tkfifcode.objects.first()
            erroe = True
            self.request.session['milad'] = 100000
            order1 = 'یک ماهه 100 هزار'
            order = self.request.session.get('amini', 100000)
            self.request.session.save()
            return render(request, 'eshtrak7.html', {'or': order, 'or2': order1, 'mimi': mimi, 'er': erroe})


class eshtrak3Month(View):
    def get(self, request):

        mimi = tkfifcode.objects.first()
        timedel = timezone.datetime.now() + timezone.timedelta(days=120)
        self.request.session['discode1'] = {'user': str(request.user), 'kaymat': int(240000), 'modate': 'سه ماهه',
                                            'tiem': str(timedel)}

        self.request.session['milad'] = 240000
        order1 = 'سه ماهه 240 هزار'
        order = self.request.session.get('amini', 240000)
        self.request.session.save()
        return render(request, 'eshtrak7.html', {'or': order, 'or2': order1, 'mimi': mimi})

    def post(self, request):
        timedel = timezone.datetime.now() + timezone.timedelta(days=120)
        code_t = self.request.session['milad']
        code = request.POST.get('code')
        t_code = tkfifcode.objects.all().first()
        if code == str(t_code):
            dis = get_object_or_404(tkfifcode, name=code)
            code_t -= code_t * dis.darsad / 100
            dis.tedad -= 1
            dis.save()
            self.request.session['discode'] = {'user': str(request.user), 'kaymat': int(code_t), 'modate': 'سه ماهه',
                                               'tiem': str(timedel)}
            self.request.session['amini'] = int(code_t)
            self.request.session.modified = True
            return redirect(request.path_info)
        else:
            mimi = tkfifcode.objects.first()
            erroe = True
            self.request.session['milad'] = 240000
            order1 = 'سه ماهه 240 هزار'
            order = self.request.session.get('amini', 240000)
            self.request.session.save()
            return render(request, 'eshtrak7.html', {'or': order, 'or2': order1, 'mimi': mimi, 'er': erroe})


class delMi(View):
    def get(self, requset):
        mi = Day1.objects.filter(user=requset.user)
        userr = User.objects.filter(phone=requset.user.phone).first()
        userr.eshtrak = False
        userr.save()
        mi.delete()
        return redirect('/')


class rezapanel(View):
    def get(self, request):
        pos = Day1.objects.all()
        amini = pos.time - timezone.timedelta(days=7)
        for milad in pos:
            print(milad.time)
            print(milad.time - timezone.timedelta(days=7))
        b = buy.objects.all()
        return render(request, 'nemodar.html', {'post': pos, 'b': b})
