# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-19 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian',
            name='ceptel',
            field=models.IntegerField(unique=True, verbose_name='Cep Tel.'),
        ),
        migrations.AlterField(
            model_name='student',
            name='okulno',
            field=models.IntegerField(unique=True, verbose_name='Okul Numarası'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tckimlik',
            field=models.IntegerField(unique=True, verbose_name='Tc Kimlik'),
        ),
    ]
