# Generated by Django 4.1.7 on 2023-05-27 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_podcast_slug_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments_post',
            name='a_id',
            field=models.IntegerField(default=0, verbose_name='پارت بندی با عدد'),
        ),
    ]
