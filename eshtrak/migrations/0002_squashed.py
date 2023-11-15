from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('eshtrak', '0001_initial')]

    initial = True

    dependencies = [
        ('acoont', '0002_squashed'),
    ]

    operations = [
        migrations.CreateModel(
            name='tkfifcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='کد تخفیف')),
                ('darsad', models.SmallIntegerField(default=0, verbose_name='درصد کد تخفیف')),
                ('tedad', models.IntegerField(default=1, verbose_name='تعداد کد تخفیف')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کد های تخفیف',
            },
        ),
        migrations.CreateModel(
            name='ssion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kaymat', models.IntegerField(default=0, verbose_name='قیمت')),
                ('modate', models.CharField(max_length=100, verbose_name='مدت زمان')),
                ('time', models.DateTimeField(default=0, verbose_name='مدت زمان باقی مانده')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سشن موفقت اشتراک',
                'verbose_name_plural': 'اشتراک های ویژه موقت',
            },
        ),
        migrations.CreateModel(
            name='Day1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kaymat', models.IntegerField(default=0, verbose_name='قیمت')),
                ('modate', models.CharField(max_length=100, verbose_name='مدت زمان')),
                ('time', models.DateTimeField(default=0, verbose_name='مدت زمان باقی مانده')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'شتراک ویژه',
                'verbose_name_plural': 'اشتراک های ویژه',
            },
        ),
    ]
