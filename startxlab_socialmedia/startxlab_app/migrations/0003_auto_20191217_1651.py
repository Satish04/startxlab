# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-17 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startxlab_app', '0002_auto_20191217_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_date',
            field=models.DateTimeField(editable=False),
        ),
    ]