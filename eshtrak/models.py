from django.db import models
from django.utils import timezone
from acoont.models import User
from post.models import post



class tkfifcode(models.Model):
    name = models.CharField(max_length=30, verbose_name='کد تخفیف', unique=True)
    darsad = models.SmallIntegerField(default=0, verbose_name='درصد کد تخفیف')
    tedad = models.IntegerField(default=1, verbose_name='تعداد کد تخفیف')

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'

    def __str__(self):
        return self.name


class Day1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    kaymat = models.IntegerField(default=0, verbose_name='قیمت')
    modate = models.CharField(max_length=100, verbose_name="مدت زمان")
    time = models.DateTimeField(default=0, verbose_name='مدت زمان باقی مانده')
    create = models.DateTimeField(auto_now_add=True)

    # time2 = models.IntegerField(default=timezone.datetime.timestamp(timezone.now()))

    class Meta:
        verbose_name = 'شتراک ویژه'
        verbose_name_plural = 'اشتراک های ویژه'


class ssion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    kaymat = models.IntegerField(default=0, verbose_name='قیمت')
    modate = models.CharField(max_length=100, verbose_name="مدت زمان")
    time = models.DateTimeField(default=0, verbose_name='مدت زمان باقی مانده')
    class Meta:
        verbose_name = 'سشن موفقت اشتراک'
        verbose_name_plural = 'اشتراک های ویژه موقت'
        
        
        
        
        
        
class buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    roman = models.ForeignKey(post, on_delete=models.CASCADE, verbose_name='رمان')
    Condition = models.BooleanField(default=False, verbose_name='وضعیت خرید')
    many = models.IntegerField(default=0, verbose_name='قیمت')

    class Meta:
        verbose_name = 'خرید تکی'
        verbose_name_plural = "خرید های تکی"

