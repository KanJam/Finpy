# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('category_name', models.CharField(max_length=30, verbose_name='Name Category')),
                ('category_description', models.TextField(max_length=150, blank=True, verbose_name='Description Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('entry_source', models.CharField(max_length=50, blank=True, verbose_name='Entry Source')),
                ('entry_value', models.DecimalField(verbose_name='Entry Value', max_digits=12, decimal_places=2)),
                ('entry_due_date', models.DateField(verbose_name='Due Date')),
                ('entry_registration_date', models.DateField(verbose_name='Registration Date')),
                ('entry_description', models.TextField(max_length=150, blank=True, verbose_name='Entry Description')),
                ('entry_quota_amount', models.PositiveIntegerField(default=1, verbose_name='Entry Quota Amount')),
                ('entry_periodicity', models.CharField(max_length=20, default='Monthly', verbose_name='Entry Periodicity Type', choices=[('Undefined', 'Undefined'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')])),
                ('entry_type', models.CharField(max_length=20, default='Expense', verbose_name='Entry Type', choices=[('Income', 'Income'), ('Expense', 'Expense')])),
                ('category', models.ForeignKey(to='Finpy.Category', verbose_name='Entry Category')),
                ('entry_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('total_entry_value', models.DecimalField(verbose_name='Total Entry Value', max_digits=12, decimal_places=2)),
                ('current_value', models.DecimalField(verbose_name='Current Entry Value', max_digits=12, decimal_places=2)),
                ('finance_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InvestmentSimulation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('present_value', models.DecimalField(blank=True, verbose_name='Present Value', max_digits=12, null=True, decimal_places=2)),
                ('future_value', models.DecimalField(blank=True, verbose_name='Future Value', max_digits=12, null=True, decimal_places=2)),
                ('payment_value', models.DecimalField(blank=True, verbose_name='Payment Value', max_digits=12, null=True, decimal_places=2)),
                ('rate_value', models.DecimalField(blank=True, verbose_name='Rate Value', max_digits=3, null=True, decimal_places=2)),
                ('period_value', models.PositiveIntegerField(default=1, blank=True, verbose_name='Period Value', null=True)),
                ('simulation_type', models.CharField(max_length=30, default='Financial Math', verbose_name='Simulation Type', choices=[('Financial Math', 'Financial Math'), ('Investment Return', 'Investment Return')])),
                ('result_to_discover', models.CharField(max_length=30, default='Future Value', verbose_name='Result To Discover', choices=[('Present Value', 'Present Value'), ('Future Value', 'Future Value'), ('Payment Value', 'Payment Value'), ('Rate Value', 'Rate Value'), ('Period Value', 'Period Value')])),
                ('simulation_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('cpf', models.CharField(max_length=14, blank=True, verbose_name='cpf', help_text='Use format ???.???.???-??', validators=[django.core.validators.RegexValidator('^[0-9]{3}\\.?[0-9]{3}\\.?[0-9]{3}\\-?[0-9]{2}$', 'Wrong Format!', 'invalid')])),
                ('job_title', models.CharField(max_length=150, blank=True, verbose_name='Job Title')),
                ('organization', models.CharField(max_length=150, blank=True, verbose_name='Organization')),
                ('expeditor_uf', models.CharField(max_length=2, default='DF', verbose_name='Expeditor', choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], blank=True)),
                ('rg', models.CharField(max_length=9, blank=True, verbose_name='rg', help_text='Use format ?.???.???', validators=[django.core.validators.RegexValidator('^[0-9]{1}\\.?[0-9]{3}\\.?[0-9]{3}$', 'Wrong Format!', 'invalid')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
