# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('Finpy', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='job_title',
            field=models.CharField(blank=True, max_length=150, verbose_name='job_title'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='organization',
            field=models.CharField(blank=True, max_length=150, verbose_name='organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cpf',
            field=models.CharField(blank=True, help_text='Use format ???.???.???-??', max_length=14, verbose_name='cpf', validators=[django.core.validators.RegexValidator('^[0-9]{3}\\.?[0-9]{3}\\.?[0-9]{3}\\-?[0-9]{2}$', 'Wrong Format!', 'invalid')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='expeditor',
            field=models.CharField(blank=True, max_length=2, verbose_name='expeditor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='rg',
            field=models.CharField(blank=True, help_text='Use format ?.???.???', max_length=9, verbose_name='rg', validators=[django.core.validators.RegexValidator('^[0-9]{1}\\.?[0-9]{3}\\.?[0-9]{3}$', 'Wrong Format!', 'invalid')]),
            preserve_default=True,
        ),
    ]
