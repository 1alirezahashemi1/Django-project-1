# Generated by Django 4.0.1 on 2022-02-28 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('taste', models.CharField(max_length=100, verbose_name='طعم')),
                ('time', models.TimeField(verbose_name='مدت زمان')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='عکس')),
            ],
        ),
    ]
