# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=30, verbose_name='Name Category')),
                ('category_description', models.TextField(max_length=150, verbose_name='Description Category', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_source', models.CharField(max_length=50, verbose_name='Entry Source', blank=True)),
                ('entry_value', models.DecimalField(verbose_name='Entry Value', max_digits=12, decimal_places=2)),
                ('entry_due_date', models.DateField(verbose_name='Due Date')),
                ('entry_registration_date', models.DateField(verbose_name='Registration Date')),
                ('entry_description', models.TextField(max_length=150, verbose_name='Entry Description', blank=True)),
                ('entry_quota_amount', models.PositiveIntegerField(default=1, verbose_name='Entry Quota Amount')),
                ('entry_periodicity', models.CharField(default='Monthly', max_length=20, verbose_name='Entry Periodicity Type', choices=[('Undefined', 'Undefined'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')])),
                ('entry_type', models.CharField(default='Expense', max_length=20, verbose_name='Entry Type', choices=[('Income', 'Income'), ('Expense', 'Expense')])),
                ('category', models.ForeignKey(verbose_name='Entry Category', to='Finpy.Category')),
                ('entry_user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_entry_value', models.DecimalField(verbose_name='Total Entry Value', max_digits=12, decimal_places=2)),
                ('current_value', models.DecimalField(verbose_name='Current Entry Value', max_digits=12, decimal_places=2)),
                ('finance_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvestimentSimulation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_invested', models.DecimalField(verbose_name='Amount Invested', max_digits=12, decimal_places=2)),
                ('taxes', models.DecimalField(verbose_name='Taxes', max_digits=5, decimal_places=2)),
                ('quota', models.PositiveIntegerField(default=1, verbose_name='Quota')),
                ('periodicity_taxes', models.CharField(default='Monthly', max_length=20, verbose_name='Taxes Periodicity Type', choices=[('Undefined', 'Undefined'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')])),
                ('quota_taxes', models.CharField(default='Monthly', max_length=20, verbose_name='Quota Periodicity Type', choices=[('Undefined', 'Undefined'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')])),
                ('finance', models.ForeignKey(verbose_name="InvestimentSimulation's Finance", to='Finpy.Finance')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpf', models.CharField(blank=True, help_text='Use format ???.???.???-??', max_length=14, verbose_name='cpf', validators=[django.core.validators.RegexValidator(b'^[0-9]{3}\\.?[0-9]{3}\\.?[0-9]{3}\\-?[0-9]{2}$', 'Wrong Format!', b'invalid')])),
                ('job_title', models.CharField(max_length=150, verbose_name='Job Title', blank=True)),
                ('organization', models.CharField(max_length=150, verbose_name='Organization', blank=True)),
                ('expeditor_uf', models.CharField(default=b'DF', max_length=2, verbose_name='Expeditor', blank=True, choices=[(b'AC', b'AC'), (b'AL', b'AL'), (b'AP', b'AP'), (b'AM', b'AM'), (b'BA', b'BA'), (b'CE', b'CE'), (b'DF', b'DF'), (b'ES', b'ES'), (b'GO', b'GO'), (b'MA', b'MA'), (b'MT', b'MT'), (b'MS', b'MS'), (b'MG', b'MG'), (b'PA', b'PA'), (b'PB', b'PB'), (b'PR', b'PR'), (b'PE', b'PE'), (b'PI', b'PI'), (b'RJ', b'RJ'), (b'RN', b'RN'), (b'RS', b'RS'), (b'RO', b'RO'), (b'RR', b'RR'), (b'SC', b'SC'), (b'SP', b'SP'), (b'SE', b'SE'), (b'TO', b'TO')])),
                ('rg', models.CharField(blank=True, help_text='Use format ?.???.???', max_length=9, verbose_name='rg', validators=[django.core.validators.RegexValidator(b'^[0-9]{1}\\.?[0-9]{3}\\.?[0-9]{3}$', 'Wrong Format!', b'invalid')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
