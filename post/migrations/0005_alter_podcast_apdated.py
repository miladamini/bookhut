# Generated by Django 4.1.7 on 2023-05-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_podcast_view_alter_post_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='apdated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
