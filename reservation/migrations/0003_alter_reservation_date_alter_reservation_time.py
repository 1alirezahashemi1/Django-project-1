# Generated by Django 4.0.1 on 2022-03-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_reservation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(verbose_name='زمان'),
        ),
    ]
