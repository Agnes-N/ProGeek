# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-07 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geek', '0003_auto_20191107_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
