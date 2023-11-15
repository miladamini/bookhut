# Generated by Django 4.2.5 on 2023-10-31 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0040_alter_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='part_roman',
            name='Pdf',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='عکس بدنه'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(auto_now_add=datetime.datetime(2023, 10, 31, 17, 25, 19, 34987, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]