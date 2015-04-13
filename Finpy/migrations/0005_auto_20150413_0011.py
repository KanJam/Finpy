# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Finpy', '0004_auto_20150412_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryRecord',
            fields=[
                ('categoryID', models.AutoField(serialize=False, primary_key=True)),
                ('nameCategory', models.CharField(max_length=30, verbose_name='Name Category')),
                ('descriptionCategory', models.TextField(max_length=150, verbose_name='Description Category', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entryID', models.AutoField(serialize=False, verbose_name='Entry Identifier', primary_key=True)),
                ('entryDueDate', models.DateField(verbose_name='Due Date')),
                ('entryRegistrationDate', models.DateField(verbose_name='Registration Date')),
                ('entryDescription', models.TextField(max_length=150, verbose_name='Entry Description', blank=True)),
                ('entryValue', models.DecimalField(verbose_name='Entry Value', max_digits=12, decimal_places=2)),
                ('entrySource', models.CharField(max_length=50, verbose_name='Entry Source', blank=True)),
                ('entryQuotaAmount', models.IntegerField(default=1, verbose_name='Entry Quota Amount')),
                ('category', models.ForeignKey(to='Finpy.CategoryRecord')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodicity',
            fields=[
                ('periodicityID', models.AutoField(serialize=False, verbose_name='Periodicity Identifier', primary_key=True)),
                ('period', models.CharField(default='Undefined', max_length=20, verbose_name='Period Type', choices=[('Undefined', 'Undefined'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Income',
        ),
        migrations.AddField(
            model_name='entry',
            name='periodicity',
            field=models.ForeignKey(to='Finpy.Periodicity'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='expeditor',
            field=models.CharField(default=b'DF', max_length=2, verbose_name='Expeditor', blank=True, choices=[(b'DF', b'DF'), (b'MG', b'MG'), (b'SP', b'SP')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='job_title',
            field=models.CharField(max_length=150, verbose_name='Job Title', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='organization',
            field=models.CharField(max_length=150, verbose_name='Organization', blank=True),
            preserve_default=True,
        ),
    ]
