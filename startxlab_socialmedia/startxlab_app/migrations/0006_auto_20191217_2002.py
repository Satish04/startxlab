# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-17 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startxlab_app', '0005_auto_20191217_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentsmodel',
            old_name='text',
            new_name='comment_text',
        ),
    ]
