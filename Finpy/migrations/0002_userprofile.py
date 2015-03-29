# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Finpy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('cpf', models.CharField(verbose_name='cpf', max_length=14, help_text='Format ???.???.???-??', validators=[django.core.validators.RegexValidator('^d{3}.d{3}.d{3}-d{2}$', 'Wrong Format!', 'invalid')])),
                ('rg', models.CharField(verbose_name='rg', max_length=9, help_text='Format ?.???.???', validators=[django.core.validators.RegexValidator('^d{1}.d{3}.d{3}$', 'Wrong Format!', 'invalid')])),
                ('expeditor', models.CharField(verbose_name='expeditor', max_length=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
