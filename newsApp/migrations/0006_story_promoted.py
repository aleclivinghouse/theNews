# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-15 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0005_story_extrawideimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='promoted',
            field=models.BooleanField(default=True),
        ),
    ]