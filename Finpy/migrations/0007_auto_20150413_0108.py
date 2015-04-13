# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finpy', '0006_auto_20150413_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodicity',
            name='period',
        ),
        migrations.AddField(
            model_name='periodicity',
            name='daysCount',
            field=models.IntegerField(verbose_name='Days count', default=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='periodicity',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Name', default='weekly'),
            preserve_default=False,
        ),
    ]
