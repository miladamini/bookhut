# Generated by Django 4.1.7 on 2023-05-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_comments_post_a_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='part_roman',
            name='a_id',
            field=models.IntegerField(default=0, verbose_name='پارت بندی با عدد'),
        ),
    ]
