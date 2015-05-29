# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Finpy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investimentsimulation',
            name='amount_invested',
        ),
        migrations.RemoveField(
            model_name='investimentsimulation',
            name='finance',
        ),
        migrations.RemoveField(
            model_name='investimentsimulation',
            name='periodicity_taxes',
        ),
        migrations.RemoveField(
            model_name='investimentsimulation',
            name='quota',
        ),
        migrations.RemoveField(
            model_name='investimentsimulation',
            name='quota_taxes',
        ),
        migrations.RemoveField(
            model_name='investimentsimulation',
            name='taxes',
        ),
        migrations.AddField(
            model_name='investimentsimulation',
            name='future_value',
            field=models.DecimalField(null=True, verbose_name='Future Value', max_digits=12, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='investimentsimulation',
            name='payment_value',
            field=models.DecimalField(null=True, verbose_name='Payment Value', max_digits=12, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='investimentsimulation',
            name='period_value',
            field=models.PositiveIntegerField(default=1, null=True, verbose_name='Period Value', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='investimentsimulation',
            name='present_value',
            field=models.DecimalField(null=True, verbose_name='Present Value', max_digits=12, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='investimentsimulation',
            name='rate_value',
            field=models.DecimalField(null=True, verbose_name='Rate Value', max_digits=3, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='investimentsimulation',
            name='simulation_type',
            field=models.CharField(default='Financial Math', max_length=30, verbose_name='Simulation Type', choices=[('Financial Math', 'Financial Math'), ('Investment Return', 'Investment Return')]),
            preserve_default=True,
        ),
    ]
