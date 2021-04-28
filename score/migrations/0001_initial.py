# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2021-04-10 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='玩家号')),
                ('get_score', models.IntegerField(verbose_name='分数')),
            ],
        ),
    ]
