# Generated by Django 4.2.5 on 2023-11-02 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0041_part_roman_pdf_alter_post_img2_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(auto_now_add=datetime.datetime(2023, 11, 2, 17, 43, 55, 792029, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]