# Generated by Django 4.0.1 on 2022-03-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='Blog', to='Blogs.Tag', verbose_name='تگ ها'),
        ),
    ]
