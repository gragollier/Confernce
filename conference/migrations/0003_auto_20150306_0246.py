# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0002_isavailable_reserved_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='isavailable',
            name='time',
        ),
        migrations.DeleteModel(
            name='IsAvailable',
        ),
        migrations.AddField(
            model_name='time',
            name='reserved_by',
            field=models.CharField(max_length=64, default='None'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='time',
            name='time_available',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
