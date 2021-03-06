# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-17 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startxlab_app', '0003_auto_20191217_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(editable=False)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
