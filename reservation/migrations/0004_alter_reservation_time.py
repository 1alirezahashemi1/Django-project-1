# Generated by Django 4.0.1 on 2022-03-10 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_reservation_date_alter_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(auto_now_add=True, verbose_name='زمان'),
        ),
    ]
