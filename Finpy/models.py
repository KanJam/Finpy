from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.


class Periodicity(models.Model):

    """Classe responsável por representar a periodicidade de uma receita/despesa"""
    """In Portuguese: Periodicidade"""

    DAILY = _('Daily') #Diário
    WEEKLY = _('Weekly') #Semanal
    MONTHLY = _('Monthly') #Mensal

    periodicityID = models.AutoField(('Periodicity Identifier'), primary_key=True)
    period = models.CharField(('Period Type'), choices=())

class Accounting(models.Model):

    """Classe responsável por manter os dados em comuns de receitas e despesas"""
    """In Portuguese: Contabil"""



class Income(models.Model):

    """Classe que representa uma receita cadastrada pelo usuário"""
    """In Portuguese: Receita"""

    incomeID = models.AutoField(('Income Identifier'), primary_key=True)
    dueDate = models.DateField(('Due Date'), editable=True, blank=True)
    salary = models.DecimalField('Salary', max_digits=10, decimal_places=2)

    def __str_(self):
        return str(self.income)


class UserProfile(models.Model):

    """Classe que representa o perfil de um usuário"""
    """In Portuguese: Perfil de Usuário"""

    user = models.OneToOneField(User)

    DF = 'DF'
    MG = 'MG'
    SP = 'SP'
    STATES = (
    (DF, 'DF'),
    (MG, 'MG'),
    (SP, 'SP'),
    )

    cpf = models.CharField(_('cpf'),max_length=14,
        help_text=_('Use format ???.???.???-??'),
        validators=[
            validators.RegexValidator(r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$',_('Wrong Format!'), 'invalid'),
        ], blank=True)
    rg = models.CharField(_('rg'),max_length=9,
        help_text=_('Use format ?.???.???'),
        validators=[
                validators.RegexValidator(r'^[0-9]{1}\.?[0-9]{3}\.?[0-9]{3}$',_('Wrong Format!'), 'invalid'),
        ], blank=True)

    expeditor = models.CharField(_('expeditor'),max_length=2, choices=STATES, default=DF, blank=True)
    job_title = models.CharField(_('job_title'), max_length=150, blank=True)
    organization = models.CharField(_('organization'), max_length=150, blank=True)


    def __str__(self):
        return self.user.username

class CategoryRecord(models.Model):

    """Classe responsável por registrar uma categoria de receita e despesa"""
    """Class responsible for registering the registry of revenues and expenses"""
    """In Portuguese: Categoria de Lançamento"""
    
    codyCategory = models.AutoField(primary_key=True);
        #Primary Key of class. Automatically Generated

    nameCategory = models.CharField(_('nameCategory'), max_length=30, blank=False)
        #Name of category recorded    
        #Name of category never should be blank

    pubDateCategory = models.DateTimeField('datePublishedCategory')
        #Date of publication of category
        
    description = models.CharField(_('nameCategory'), max_length=150, blank=True)
        #Detail of category recorded
        #Is not required    
