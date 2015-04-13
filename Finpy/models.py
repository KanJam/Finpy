from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.


class Income(models.Model):

    salary = models.DecimalField('Salary', max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.salary)


class UserProfile(models.Model):
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

    """Class responsible for registering the registry of revenues and expenses"""
    """In Portuguese: Categoria de Lançamento"""
    
    nameCategory = models.CharField(_('nameCategory'), max_length=30, blank=False)
        #Name of category recorded    
        #Name of category never should be blank
        
    description = models.CharField(_('nameCategory'), max_length=150, blank=True)
        #Detail of category recorded
        #Is not required    
