from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from acoont.models import User
from post.models import post


class Advertise(models.Model):
    id_fild = models.IntegerField(verbose_name='ایدی تبلیغ')
    img = models.ImageField(verbose_name="عکس تبلیغ")
    title = RichTextField(verbose_name='توضیحات')

    title_dokme = models.CharField(max_length=50, verbose_name='متن دکمه')
    link = models.CharField(max_length=900, verbose_name="لینک تبلیغ")
    crated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نبلیغات'
        verbose_name_plural = 'تبلیغات ها'
class Hmtext(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=100, verbose_name='اسم کاربر')
    text = models.TextField(verbose_name='توضیحات')
    file = models.FileField(verbose_name='فایل', null=True, blank=True, upload_to='hmkari')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'همکاری با ما'
        verbose_name_plural = 'همکاری ها باما'
        
        
        
        
        
class Autherroman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=100, verbose_name='اسم کاربر')
    text = models.TextField(verbose_name='توضیحات')
    file = models.FileField(verbose_name='عکس ارسالی', null=True, blank=True, upload_to='autherroman')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'درخواست حذف رمان'
        verbose_name_plural = 'درخواست های حذف رمان'
        
        
        
        
        
class Competition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    roman = models.CharField(max_length=150, verbose_name='رمان')
    text = models.TextField()
    bol = models.BooleanField(default=False,verbose_name='جواب درست')

    class Meta:
        verbose_name = 'جایزه'
        verbose_name_plural = 'جوایز'
        
        
        
        
        
        
class UserJvayez(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    roman = models.ForeignKey(post, on_delete=models.CASCADE, verbose_name='رمان')
    Condition = models.BooleanField(default=False, verbose_name=' شکرت کرده در مسابقات جوایز رمان')

    class Meta:
        verbose_name = 'شرکت کنند جوایز'
        verbose_name_plural = "شرکت کنندگان جوایز"


class Questions(models.Model):
    roman = models.ForeignKey(post, on_delete=models.CASCADE, verbose_name="رمان")
    text = RichTextField(verbose_name='سوالات رمان')

    class Meta:
        verbose_name = 'سوال رمان'
        verbose_name_plural = 'سوالات رمان ها'
        
        
        
        
        
        
        
        
        
class abutsaznde(models.Model):
    name = models.CharField(max_length=300, verbose_name='اسم')
    title = models.CharField(max_length=300, verbose_name='متن')
    img = models.ImageField(verbose_name="عکس")
    body = RichTextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'عکس مالک'
        verbose_name_plural = "عکس های مالک"


class abutkarbar(models.Model):
    title = models.CharField(max_length=300, verbose_name='اسم')
    img = models.ImageField(verbose_name="عکس")
    body = models.CharField(max_length=300, verbose_name='وظیفه')

    class Meta:
        verbose_name = 'عکس کارکنان'
        verbose_name_plural = "عکس های کارکنان"

