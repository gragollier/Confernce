# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='isavailable',
            name='reserved_by',
            field=models.CharField(default='None', max_length=64),
            preserve_default=True,
        ),
    ]
