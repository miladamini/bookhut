from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('acoont', '0001_initial')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=80, verbose_name='نام کاربری')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='شماره تلفن')),
                ('blok', models.BooleanField(default=False, verbose_name='بلاک')),
                ('eshtrak', models.BooleanField(default=False, verbose_name='اشتراک ویژه')),
                ('day', models.IntegerField(default=0, verbose_name='روز های اشتراک')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=11)),
                ('code', models.SmallIntegerField()),
                ('expiration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'کد تایید',
                'verbose_name_plural': 'کد های تایید',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=12)),
                ('postal_code', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ادرس',
                'verbose_name_plural': 'ادرس ها',
            },
        ),
    ]
