# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-20 10:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151220_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-post_time',), 'permissions': (('change_foreign_blogpost', "Edit someone else's post"), ('add_media_to_blogpost', 'Upload media to a blog post'))},
        ),
    ]
