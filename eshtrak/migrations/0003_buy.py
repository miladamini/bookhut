# Generated by Django 4.1.7 on 2023-06-12 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0012_post_buy_rom'),
        ('eshtrak', '0002_squashed'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Condition', models.BooleanField(default=False, verbose_name='وضعیت خرید')),
                ('many', models.IntegerField(default=0, verbose_name='قیمت')),
                ('roman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='رمان')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'خرید تکی',
                'verbose_name_plural': 'خرید های تکی',
            },
        ),
    ]
