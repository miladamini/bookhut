from django.db import models
from acoont.models import User
from ckeditor.fields import RichTextField
from jalali_date import datetime2jalali, date2jalali
from django.utils import timezone


# Create your models here.


class post(models.Model):
    correction_model = [
        ('1', 'عاشقانه'),
        ('2', 'ترسناک'),
        ('3', 'فانتزی'),
        ('4', 'کوتاه'),
        ('5', 'اجتماعی'),
        ('6', 'طنز'),
        ('7', 'پلیسی'),
        ('8', 'BDSM'),
    ]
    correction_model2 = [
        ('به اتمام رسیده', 'به اتمام رسیده'),
        ('در حال ادامه', 'در حال ادامه'),

    ]
    correction = models.CharField(max_length=100, choices=correction_model, verbose_name='ژانر')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده',
                               limit_choices_to={'is_admin' or 'part' or 'roman_admin' or 'coment_admin': True})
    title = models.CharField(max_length=100)
    body = models.TextField(verbose_name='توضیحات شماره یک')
    img = models.ImageField(verbose_name="عکس کاور", upload_to='img')
    img2 = models.ImageField(verbose_name="عکس بدنه", upload_to='img', null=True, blank=True)
    pdf = models.FileField(upload_to='pdf', null=True, blank=True, verbose_name='فایل PDF')
    body2 = RichTextField(blank=True, null=True, verbose_name='توضیحات شماره دو')
    Accepted = models.BooleanField(default=False, verbose_name="تایید شده")
    created = models.DateTimeField(auto_now_add=True)
    apdated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, verbose_name="لینک صفحه رمان")
    link_p = models.CharField(max_length=500, null=True, verbose_name="لینک دانلود اول")
    link_d = models.CharField(max_length=500, null=True, verbose_name='لینک دانلود دوم')
    alt = models.CharField(max_length=500, null=True, blank=True, verbose_name='توضیحات عکس')
    eshtrak = models.BooleanField(default=False, verbose_name='اشتراک ویژه')
    buy_rom = models.IntegerField(default=0, verbose_name="قیمت")
    javyez = models.BooleanField(default=False, verbose_name='رمان جایزه دار')
    imgProf = models.ImageField(null=True, blank=True, verbose_name='عکس نویسنده')
    name = models.CharField(max_length=900, null=True, blank=True, verbose_name='اسم نویسنده')
    Condition = models.CharField(max_length=100, null=True, blank=True, choices=correction_model2,
                                 verbose_name='وضغیت رمان')

    view = models.IntegerField(default=1, verbose_name='بازدید')
    time = models.TimeField(auto_now_add=timezone.now(), null=True, blank=True)
    botmodel = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

        verbose_name = 'رمان'
        verbose_name_plural = 'رمان ها'

    def __str__(self):
        return self.title


class Podcast(models.Model):
    correction_model = [
        ('1', 'کتاب صوتی'),
        ('2', 'پادکست'),
        ('3', 'رمان صوتی'),
    ]
    correction = models.CharField(max_length=100, choices=correction_model, verbose_name='دسته بندی')
    view = models.IntegerField(default=1, verbose_name='بازدید')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده',
                               limit_choices_to={'is_admin' or 'part' or 'roman_admin' or 'coment_admin': True})
    title = models.CharField(max_length=100)
    body = models.TextField(verbose_name="توضیحات")
    img = models.ImageField(null=True, blank=True, verbose_name="عکس", upload_to='img')
    music = models.FileField(upload_to='Music', null=True, blank=True, verbose_name="فایل پادکست")
    Accepted = models.BooleanField(default=False, verbose_name="تایید شده")
    created = models.DateTimeField(auto_now_add=True)
    apdated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(allow_unicode=True, unique=True, verbose_name="لینک صفحه رمان")
    link_p = models.CharField(max_length=500, null=True, verbose_name='لینک پخش ')
    link_d = models.CharField(max_length=500, null=True, verbose_name="لینک دانلود")
    alt = models.CharField(max_length=500, null=True, blank=True, verbose_name='توضیحات عکس')
    eshtrak = models.BooleanField(default=False, verbose_name='اشتراک ویژه')
    botmodel = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

        verbose_name = 'پادکست'
        verbose_name_plural = 'پادکست ها'

    def __str__(self):
        return self.title


class Comments_post(models.Model):
    articel = models.ForeignKey(post, null=True, blank=True, on_delete=models.CASCADE, related_name='comments',
                                verbose_name="رمان والد")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    name = models.CharField(max_length=50, null=True, verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='riplay',
                               verbose_name="ریپلای")
    text = models.TextField(null=True, verbose_name="متن")
    created_ad = models.DateTimeField(auto_now_add=True)
    apdated = models.DateField(auto_now=True)
    a_id = models.IntegerField(default=0, verbose_name='پارت بندی با عدد')
    user_admin = models.BooleanField(default=False, verbose_name='ادمین بودن کاربر')

    def __str__(self):
        return self.text

    @property
    def comment_count(self):
        return self.comment_set.count()

    class Meta:
        verbose_name = 'کامت رمان'
        verbose_name_plural = 'کامنت های رمان'


class Comments_Podcast(models.Model):
    articel = models.ForeignKey(Podcast, null=True, on_delete=models.CASCADE, related_name='comments',
                                verbose_name="رمان والد")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=50, null=True, verbose_name='اسم')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='riplay',
                               verbose_name="ریپلای")
    text = RichTextField(verbose_name="متن")
    created_ad = models.DateTimeField(auto_now_add=True)
    apdated = models.DateField(auto_now=True)

    def __str__(self):
        return self.text

    @property
    def comment_count(self):
        return self.comment_set.count()

    class Meta:
        verbose_name = 'کامنت پادکست'
        verbose_name_plural = 'کامنت های پادکست'


class Tamas_ba_ma(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=50, null=True, verbose_name='اسم')
    text = models.TextField(null=True, verbose_name="متن")
    created_ad = models.DateTimeField(auto_now_add=True)
    apdated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس های باما'


class Part_roman(models.Model):
    roman = models.ForeignKey(post, on_delete=models.CASCADE, verbose_name='رمان والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')

    body = RichTextField(verbose_name="متن رمان")
    name = models.CharField(max_length=50, verbose_name="اسم پارت")
    created_ad = models.DateTimeField(auto_now_add=True)
    apdated = models.DateField(auto_now=True)
    a_id = models.IntegerField(default=0, verbose_name='پارت بندی با عدد')
    Pdf = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'پارت بندی رمان'
        verbose_name_plural = 'پارت بندی رمان ها'

    def __str__(self):
        return f'{self.roman}--{self.name}'

    def miladtime(self):
        return date2jalali(self.created_ad)


class Part_pad(models.Model):
    pad = models.ForeignKey(Podcast, on_delete=models.CASCADE, verbose_name='پادکست والد')
    body = models.TextField(verbose_name="متن پادکست")
    name = models.CharField(max_length=50, verbose_name="اسم ")
    link = models.CharField(max_length=1000, verbose_name='لینک رمان')
    created_ad = models.DateTimeField(auto_now_add=True)
    apdated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'زیر مجموعه پادکست'
        verbose_name_plural = 'زیر مجموعه پادکست ها'

    def __str__(self):
        return f'{self.pad}--{self.name}'
