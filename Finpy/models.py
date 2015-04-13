from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.


class Periodicity(models.Model):

    """Classe responsavel por representar a periodicidade de uma receita/despesa"""
    """In Portuguese: Periodicidade"""

    UNDEFINED = _('Undefined')
    DAILY = _('Daily') #Diario
    WEEKLY = _('Weekly') #Semanal
    MONTHLY = _('Monthly') #Mensal

    PERIODICITY = (
    (UNDEFINED, _('Undefined')),
    (DAILY, _('Daily')),
    (WEEKLY, _('Weekly')),
    (MONTHLY, _('Monthly')),
    )

    periodicityID = models.AutoField(_('Periodicity Identifier'), primary_key=True)

    name = models.CharField(_('Name'), choices=PERIODICITY, max_length=20)

    daysCount = models.IntegerField(_('Days count'), default = 30)

    def __str__(self):
        return self.name


class CategoryRecord(models.Model):

    """Classe responsavel por registrar uma categoria de receita e despesa"""
    """Class responsible for registering the registry of revenues and expenses"""
    """In Portuguese: Categoria de Lancamento"""

    categoryID = models.AutoField(primary_key=True);
        #Primary Key of class. Automatically Generated

    nameCategory = models.CharField(_('Name Category'), max_length=30, blank=False)
        #Name of category recorded
        #Name of category never should be blank

    descriptionCategory = models.TextField(_('Description Category'), max_length=150, blank=True)
        #Detail of category recorded
        #Is not required

    def __str__(self):
        return self.nameCategory

class Entry(models.Model):

    """Classe responsavel por manter os dados em comuns de receitas e despesas"""
    """In Portuguese: Contabil"""

    INCOME = _('Income')
    EXPENSE = _('Expense')

    OPTIONS = (
    (INCOME, _('Income')),
    (EXPENSE, _('Expense')),
    )

    entryID = models.AutoField(_('Entry Identifier'), primary_key=True)
        #Chave primaria

    entryDueDate = models.DateField(_('Due Date'))
        #Data de pagamento.

    entryRegistrationDate = models.DateField(_('Registration Date'))
        #Date registration of accounting

    entryDescription = models.TextField(_('Entry Description'), max_length=150, blank=True)
        #Descricao de uma contabil

    entryValue = models.DecimalField(_('Entry Value'), decimal_places=2, max_digits=12)
        #Registro do valor do contabel

    entrySource = models.CharField(_('Entry Source'), max_length=50, blank=True)
        #Empresa/Organizacao/Entidade fonte da requisicao do contabil

    entryQuotaAmount = models.IntegerField(_('Entry Quota Amount'), default=1)
        #Quantidade de parcelas

    entryType = models.CharField(_('Entry Type'), choices=OPTIONS, max_length=20)

    periodicity = models.ForeignKey(Periodicity)
        #Relacionamento de 1 pra n com Periodicidade

    user = models.ForeignKey(User)
        #Relacionamento de 1 pra n com Usuario

    category = models.ForeignKey(CategoryRecord)
        #Relacionamento de 1 pra n com Categoria de lancamento

    def __str__(self):
        return self.entryDescription


class UserProfile(models.Model):

    """Classe que representa o perfil de um usuario"""
    """In Portuguese: Perfil de Usuario"""

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

    expeditor = models.CharField(_('Expeditor'),max_length=2, choices=STATES, default=DF, blank=True)
    job_title = models.CharField(_('Job Title'), max_length=150, blank=True)
    organization = models.CharField(_('Organization'), max_length=150, blank=True)

    def __str__(self):
        return self.user.username
