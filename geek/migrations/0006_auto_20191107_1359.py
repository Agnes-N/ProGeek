# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-07 11:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geek', '0005_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='partner_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geek.Programmers_profile'),
        ),
        migrations.AddField(
            model_name='partner',
            name='partner_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
