# Generated by Django 4.2.5 on 2023-09-07 18:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_abutkarbar_abutsaznde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='title_dokme',
            field=ckeditor.fields.RichTextField(verbose_name='متن دکمه'),
        ),
    ]