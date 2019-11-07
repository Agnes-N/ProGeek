# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-07 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geek', '0002_chat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='posred_date',
            new_name='posted_date',
        ),
        migrations.RemoveField(
            model_name='programmers_profile',
            name='date',
        ),
        migrations.AddField(
            model_name='programmers_profile',
            name='bio',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='programmers_profile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
