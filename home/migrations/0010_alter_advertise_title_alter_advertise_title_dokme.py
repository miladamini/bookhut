# Generated by Django 4.2.5 on 2023-09-07 18:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_advertise_title_dokme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='title',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='title_dokme',
            field=models.CharField(max_length=50, verbose_name='متن دکمه'),
        ),
    ]
