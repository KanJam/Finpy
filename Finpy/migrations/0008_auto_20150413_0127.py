# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finpy', '0007_auto_20150413_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entryType',
            field=models.CharField(verbose_name='Entry Type', default='Income', max_length=20, choices=[('Income', 'Income'), ('Expense', 'Expense')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='periodicity',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=20, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')]),
            preserve_default=True,
        ),
    ]
