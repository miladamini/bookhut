# Generated by Django 4.2.5 on 2023-10-17 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_alter_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='botmodel',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='botmodel',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(auto_now_add=datetime.datetime(2023, 10, 17, 9, 43, 8, 534457, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
