from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('home', '0001_initial'), ('home', '0002_hmtext')]

    initial = True

    dependencies = [
        ('acoont', '0002_squashed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='عکس تبلیغ')),
                ('title', models.CharField(max_length=50, verbose_name='تایتل')),
                ('title_dokme', models.CharField(max_length=50, verbose_name='متن دکمه')),
                ('link', models.CharField(max_length=900, verbose_name='لینک تبلیغ')),
                ('crated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'نبلیغات',
                'verbose_name_plural': 'تبلیغات ها',
            },
        ),
        migrations.CreateModel(
            name='Hmtext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم کاربر')),
                ('text', models.TextField(verbose_name='توضیحات')),
                ('file', models.FileField(blank=True, null=True, upload_to='hmkari', verbose_name='فایل')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'همکاری با ما',
                'verbose_name_plural': 'همکاری ها باما',
            },
        ),
    ]
