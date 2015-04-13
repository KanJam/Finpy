# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finpy', '0005_auto_20150413_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='expeditor',
            field=models.CharField(choices=[('DF', 'DF'), ('MG', 'MG'), ('SP', 'SP')], max_length=2, default='DF', verbose_name='Expeditor', blank=True),
            preserve_default=True,
        ),
    ]
