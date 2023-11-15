from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser
)


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an phone address')

        user = self.model(
            phone=self.normalize_email(phone),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = models.CharField(
        verbose_name='شماره تلفن',
        max_length=12,
        unique=True,

    )
    username = models.CharField(max_length=80, verbose_name='نام کاربری')
    phone = models.CharField(max_length=12, unique=True, verbose_name='شماره تلفن')
    blok = models.BooleanField(default=False, verbose_name='بلاک')
    eshtrak = models.BooleanField(default=False, verbose_name='اشتراک ویژه')
    day = models.IntegerField(default=0, verbose_name='روز های اشتراک')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    roman_admin = models.BooleanField(default=False, verbose_name="ادمین رمان ها")
    coment_admin = models.BooleanField(default=False, verbose_name='ادمین کامنت ها')
    part = models.BooleanField(default=False, verbose_name='ادمین پارت بندی ها')
    img = models.ImageField(verbose_name='عکس', upload_to='img/prof', null=True, blank=True)
    email = models.EmailField(verbose_name='email', null=True, blank=True)
    buo = models.CharField(max_length=500, verbose_name='بیوگرافی', null=True, blank=True)
    facebook = models.URLField(blank=True, null=True, verbose_name='اکانت فیس بوک')
    airbnb = models.URLField(blank=True, null=True, verbose_name='سایت اکانت ها')
    twitter = models.URLField(blank=True, null=True, verbose_name='اکانت تویتر')
    instagram = models.URLField(blank=True, null=True, verbose_name='اکانت اینستاگرام')
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.img:
            self.img = 'image.jpg'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class otp(models.Model):
    token = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'کد تایید'
        verbose_name_plural = 'کد های تایید'


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Order')
    follname = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12)
    postal_code = models.CharField(max_length=50)

    def __str__(self):
        return self.user.phone

    class Meta:
        verbose_name = 'ادرس'
        verbose_name_plural = 'ادرس ها'


class user_part(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    kole_part = models.IntegerField(verbose_name='کل پارت های  گذاشته شده')
    padakt_part = models.IntegerField(null=True, blank=True, default=0, verbose_name='پارت های پرداخت شده')
    bki_part = models.IntegerField(null=True, blank=True, default=0, verbose_name='پارت های پرداخت نشده')

    class Meta:
        verbose_name = 'تعداد پارت کاربر'
        verbose_name_plural = 'تعداد پارت های کاربران'
