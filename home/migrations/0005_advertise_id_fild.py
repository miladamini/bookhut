# Generated by Django 4.1.7 on 2023-05-24 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_autherroman'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='id_fild',
            field=models.IntegerField(default=1, verbose_name='ایدی تبلیغ'),
            preserve_default=False,
        ),
    ]
