# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('salary', models.DecimalField(verbose_name='Salary', decimal_places=2, max_digits=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
