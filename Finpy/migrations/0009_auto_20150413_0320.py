# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finpy', '0008_auto_20150413_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='periodicity',
            field=models.ForeignKey(blank=True, to='Finpy.Periodicity'),
            preserve_default=True,
        ),
    ]
