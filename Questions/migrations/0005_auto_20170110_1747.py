# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0004_auto_20170110_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='FirstName',
            field=models.CharField(max_length=50, null=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='LastName',
            field=models.CharField(max_length=50, null=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='Login',
            field=models.CharField(max_length=50, null=None, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(max_length=50, null=None),
        ),
    ]
