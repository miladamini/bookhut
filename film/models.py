from django.db import models
from ckeditor.fields import RichTextField

from acoont.models import User


# Create your models here.

class FilmModel(models.Model):
    slug = models.SlugField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=90)
    body = RichTextField(blank=True, null=True, verbose_name='توضیحات')
    img = models.ImageField(verbose_name="عکس بدنه", upload_to='img')

    class Meta:
        verbose_name = 'اموزش نویسندگی'
        verbose_name_plural = 'اموزش های نویسندگی'

    def __str__(self):
        return self.title


class zerfilm(models.Model):
    father = models.ForeignKey(FilmModel, on_delete=models.CASCADE, verbose_name='زیر مجموعه')
    title = models.CharField(max_length=90)
    link = models.URLField(verbose_name="لینک فیلم")
    a_id = models.IntegerField(default=0, verbose_name='قسمت بندی اموزش ها')

    class Meta:
        verbose_name = 'قسمت اموزش'
        verbose_name_plural = 'قسمت های اموزش'

    def __str__(self):
        return self.title


class Comments_film(models.Model):
    articel = models.ForeignKey(FilmModel, null=True, blank=True, on_delete=models.CASCADE, related_name='comments',
                                verbose_name="اموزش والد")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=50, null=True, verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='riplay',
                               verbose_name="ریپلای")
    text = models.TextField(null=True, verbose_name="متن")
    created_ad = models.DateTimeField(auto_now_add=True)
    apdated = models.DateField(auto_now=True)
    user_admin = models.BooleanField(default=False, verbose_name='ادمین بودن کاربر')



    def __str__(self):
        return self.text

    @property
    def comment_count(self):
        return self.comment_set.count()

    class Meta:
        verbose_name = 'کامت آموزش'
        verbose_name_plural = 'کامنت های آموزش'
