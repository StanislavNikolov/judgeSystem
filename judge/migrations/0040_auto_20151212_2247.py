# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-12 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0039_auto_20151210_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testgroupresult',
            name='score',
        ),
        migrations.AddField(
            model_name='testgroupresult',
            name='passed',
            field=models.BooleanField(default=False),
        ),
    ]
