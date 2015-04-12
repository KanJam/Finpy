# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finpy', '0003_auto_20150329_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='expeditor',
            field=models.CharField(default=b'DF', max_length=2, verbose_name='expeditor', blank=True, choices=[(b'DF', b'DF'), (b'MG', b'MG'), (b'SP', b'SP')]),
            preserve_default=True,
        ),
    ]
