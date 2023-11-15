from django.db import models
from acoont.models import User
from django.utils import timezone
from jalali_date import datetime2jalali, date2jalali


# Create your models here.


class Chatemodel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=200)
    img = models.ImageField()
    body = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تاپیک'
        verbose_name_plural = 'تاپیک ها'


class UserChatModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    chat_m = models.ForeignKey(Chatemodel, on_delete=models.CASCADE, verbose_name='تاپیک')
    text = models.TextField(verbose_name='متن پیام')
    replay = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='riplay',
                               verbose_name="ریپلای")
    p_time = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.text

    def miladtime(self):
        return datetime2jalali(self.created_ad)

    class Meta:
        verbose_name = 'چت کاربر'
        verbose_name_plural = 'چت های کابران'
