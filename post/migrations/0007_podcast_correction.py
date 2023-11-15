# Generated by Django 4.1.7 on 2023-05-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_correction'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='correction',
            field=models.CharField(choices=[('1', 'کتاب صوتی'), ('2', 'پادکست'), ('3', 'رمان صوتی')], default=1, max_length=100, verbose_name='دسته بندی'),
            preserve_default=False,
        ),
    ]
