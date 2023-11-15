# Generated by Django 4.2.5 on 2023-10-23 15:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات')),
                ('img', models.ImageField(upload_to='img', verbose_name='عکس بدنه')),
            ],
            options={
                'verbose_name': 'اموزش نویسندگی',
                'verbose_name_plural': 'اموزش های نویسندگی',
            },
        ),
    ]
