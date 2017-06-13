# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 06:39
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import sorl_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_auto_20170613_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', sorl.thumbnail.fields.ImageField(upload_to='gallery', verbose_name='изображение галереи')),
                ('img_crop', sorl_cropping.fields.ImageRatioField(blank=True, help_text=None, image_field='img', max_length=255, size='206x140')),
                ('text', models.TextField(verbose_name='Текс')),
                ('cdate', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('pdate', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('prior', models.IntegerField(default=0, verbose_name='приоритет порядка отображения')),
                ('active', models.BooleanField(default=True, verbose_name='Активное')),
            ],
        ),
    ]