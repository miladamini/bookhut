# Generated by Django 4.2.5 on 2023-09-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoont', '0008_alter_user_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='airbnb',
            field=models.URLField(blank=True, null=True, verbose_name='سایت اکانت ها'),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='اکانت فیس بوک'),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='اکانت اینستاگرام'),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='اکانت تویتر'),
        ),
    ]