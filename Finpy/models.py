from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core import validators
from django.contrib.auth.models import User

class UserProfile(models.Model):

    """Classe UserProfile. Classe que possui
    as informações inerentes ao Perfil do Usuário.
    Realiza extensão da Model fornecida pelo próprio
    framework Django com informações básicas de usuário.
    """

    # Usuario Associado
    user = models.OneToOneField(User)

    # Valores possiveis para Estado
    AC = 'AC'
    AL = 'AL'
    AP = 'AP'
    AM = 'AM'
    BA = 'BA'
    CE = 'CE'
    DF = 'DF'
    ES = 'ES'
    GO = 'GO'
    MA = 'MA'
    MT = 'MT'
    MS = 'MS'
    MG = 'MG'
    PA = 'PA'
    PB = 'PB'
    PR = 'PR'
    PE = 'PE'
    PI = 'PI'
    RJ = 'RJ'
    RN = 'RN'
    RS = 'RS'
    RO = 'RO'
    RR = 'RR'
    SC = 'SC'
    SP = 'SP'
    SE = 'SE'
    TO = 'TO'

    # Enum de Estados
    STATES = (
    (AC, 'AC'),
    (AL, 'AL'),
    (AP, 'AP'),
    (AM, 'AM'),
    (BA, 'BA'),
    (CE, 'CE'),
    (DF, 'DF'),
    (ES, 'ES'),
    (GO, 'GO'),
    (MA, 'MA'),
    (MT, 'MT'),
    (MS, 'MS'),
    (MG, 'MG'),
    (PA, 'PA'),
    (PB, 'PB'),
    (PR, 'PR'),
    (PE, 'PE'),
    (PI, 'PI'),
    (RJ, 'RJ'),
    (RN, 'RN'),
    (RS, 'RS'),
    (RO, 'RO'),
    (RR, 'RR'),
    (SC, 'SC'),
    (SP, 'SP'),
    (SE, 'SE'),
    (TO, 'TO')
    )
    
    # CPF
    cpf = models.CharField(_('cpf'),max_length=14,
        help_text=_('Use format ???.???.???-??'),
        validators=[
            validators.RegexValidator(r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$',_('Wrong Format!'), 'invalid'),
        ], blank=True)
    
    # Profissao
    job_title = models.CharField(_('Job Title'), max_length=150, blank=True)
    
    # Organizacao onde Trabalha
    organization = models.CharField(_('Organization'), max_length=150, blank=True)
    
    # Estado do Orgao Expedidor do RG
    expeditor_uf = models.CharField(_('Expeditor'),max_length=2, choices=STATES, default=DF, blank=True)
    
    # RG
    rg = models.CharField(_('rg'),max_length=9,
        help_text=_('Use format ?.???.???'),
        validators=[
                validators.RegexValidator(r'^[0-9]{1}\.?[0-9]{3}\.?[0-9]{3}$',_('Wrong Format!'), 'invalid'),
        ], blank=True)

    
    def __str__(self):
        
        """Método de conversão para
        o formato string.
        """

        return self.user.username

class Finance(models.Model):

    """Classe Finance. Classe que possui informações
    inerentes aos lançamentos de receitas e despesas, tais
    como periodicidade, vinculação de um lançamento à um determinado
    usuário e valores de capital.
    """

    # Usuario Associado
    finance_user = models.OneToOneField(User)

    # Valor Total de Lancamentos
    total_entry_value = models.DecimalField(_('Total Entry Value'), decimal_places=2, max_digits=12)
    # Caixa Atual
    current_value = models.DecimalField(_('Current Entry Value'), decimal_places=2, max_digits=12)

    # Valores Possiveis de Periodicidade
    UNDEFINED = _('Undefined')
    DAILY = _('Daily') # Diario
    WEEKLY = _('Weekly') # Semanal
    MONTHLY = _('Monthly') # Mensal

    # Enum de Periodicidade
    PERIODICITY = (
    (UNDEFINED, _('Undefined')),
    (DAILY, _('Daily')),
    (WEEKLY, _('Weekly')),
    (MONTHLY, _('Monthly')),
    )

    def __str__(self):
        
        """Método de conversão para
        o formato string.
        """

        return self.current_value

class InvestmentSimulation(models.Model):

    """Classe InvestmentSimulation. Classe que possui as informações
    inerentes às simulações de investimento, tanto no âmbito de
    Matemática Financeira, como também, na perspectiva de Análise
    de Retorno de Investimentos.
    """

    # Valor presente do investimento
    present_value = models.DecimalField(_('Present Value'), decimal_places=2, max_digits=12, blank=True, null=True)

    # Valor futuro do investimento
    future_value = models.DecimalField(_('Future Value'), decimal_places=2, max_digits=12, blank=True, null=True)

    # Valor do pagamento utilizado na simulacao
    payment_value = models.DecimalField(_('Payment Value'), decimal_places=2, max_digits=12, blank=True, null=True)
 
    # Valor da taxa
    rate_value = models.DecimalField(_('Rate Value'), decimal_places=2, max_digits=3, blank=True, null=True)   
    
    # Tempo de duracao do investimento
    period_value = models.PositiveIntegerField(_('Period Value'), default=1, blank=True, null=True)

    # Itens do Enum Resultado A Descobrir
    PRESENT_VALUE = _('Present Value')
    FUTURE_VALUE = _('Future Value')
    PAYMENT_VALUE = _('Payment Value')
    RATE_VALUE = _('Rate Value')
    PERIOD_VALUE = _('Period Value')

    # Enum do Tipo Resultado A Descobrir
    RESULT_TO_DISCOVER = (
    (PRESENT_VALUE, _('Present Value')),
    (FUTURE_VALUE, _('Future Value')),
    (PAYMENT_VALUE, _('Payment Value')),
    (RATE_VALUE, _('Rate Value')),
    (PERIOD_VALUE, _('Period Value')),
    )

    # Itens do Enum Tipo de Simulacao
    FINANCIAL_MATH = _('Financial Math')
    INVESTMENT_RETURN = _('Investment Return')

    # Enum de Tipo de Simulacao
    SIMULATION_TYPE = (
    (FINANCIAL_MATH, _('Financial Math')),
    (INVESTMENT_RETURN, _('Investment Return')),
    )

    # Definicao do tipo de investimento
    simulation_type = models.CharField(_('Simulation Type'), choices=SIMULATION_TYPE, default=FINANCIAL_MATH, max_length=30)

    # Definicao do resultado a descobrir
    result_to_discover = models.CharField(_('Result To Discover'), choices=RESULT_TO_DISCOVER, default=FUTURE_VALUE, max_length=30)

    simulation_user = models.ForeignKey(User, verbose_name=_('User'))

    def calculate_investment(self):
        
        """Método que verifica os parâmetros de simulação
        passados pelo usuário e dispara o método adequado para
        o cálculo de um dos elementos pertencentes aos módulos
        de Engenharia Econômica (Matemática Financeira ou Análise de Retorno de Investimento).
        """

        return SimulationAbstractStrategy.calculate_investment(self)

    def __str__(self):

        """Método de conversão para
        o formato string.
        """

        return str(self.present_value)

class SimulationAbstractStrategy:

    """Classe SimulationAbstractStrategy. Classe Abstrata construída
    para aplicação dos Padrões de Projeto GoF Comportamentais Template
    Method e Strategy. Possui a definição da assinatura dos métodos de 
    validação dos resultados e construção dos passos para as operações 
    de simulação de investimentos.
    """

    def calculate_investment(simulation_investment):

        """Método que, dado uma instância de InvestmentSimulation, verifica
        o módulo de Engenharia Econômica para a simulação requerida pelo
        usuário. No caso de Matemática Financeira, por exemplo, dependendo dos
        campos preenchidos pelo usuário, poderá ser calculado Valor Presente ou
        Valor Futuro. No âmbito de Análise de Retorno de Investimento, tem-se o 
        cálculo do PayBack (Tempo de retorno de um investimento).
        """

        if simulation_investment.simulation_type == InvestmentSimulation.FINANCIAL_MATH:
            if simulation_investment.result_to_discover == InvestmentSimulation.PRESENT_VALUE:
                result_list = PresentValueStrategy.calculate_steps(simulation_investment)
                PresentValueStrategy.validate_result(simulation_investment,result_list[-1])
            elif simulation_investment.result_to_discover == InvestmentSimulation.FUTURE_VALUE:
                result_list = FutureValueStrategy.calculate_steps(simulation_investment)
                FutureValueStrategy.validate_result(simulation_investment,result_list[-1])
        elif simulation_investment.simulation_type == InvestmentSimulation.INVESTMENT_RETURN:
        	if simulation_investment.result_to_discover == InvestmentSimulation.PERIOD_VALUE:
        		result_list = PayBackStrategy.calculate_steps(simulation_investment)
        		PayBackStrategy.validate_result(simulation_investment, result_list[0])
        return result_list

    def calculate_steps(simulation_investment): pass

    def validate_result(simulation_investment,result): pass

class PresentValueStrategy(SimulationAbstractStrategy):

    """Classe PresentValueStrategy. Classe que realiza 
    extensão da Classe SimulationAbstractStrategy e formaliza
    todos os comportamentos no âmbito do cálculo do Valor Presente.
    """

    def calculate_steps(simulation_investment):

        """Método que preenche uma lista com o 
        resultado de cada iteração do cálculo de
        Valor Presente.
        """

        result = fv = simulation_investment.future_value
        period = simulation_investment.period_value
        rate = simulation_investment.rate_value/100
        result_list = [fv]
        for k in range(1, period):
            result = fv/((1 + rate)**k)
            result_list.append(result)
        return result_list

    def validate_result(simulation_investment,result):

        """Método que verifica se último valor da iteração
        de cálculos do Valor Presente condiz com a aplicação
        direta da equação para o período fornecido.
        """

        fv = simulation_investment.future_value
        period = simulation_investment.period_value
        rate = simulation_investment.rate_value/100
        return fv/((1 + rate)**period) == result


class FutureValueStrategy(SimulationAbstractStrategy):

    """Classe FutureValueStrategy. Classe que realiza 
    extensão da Classe SimulationAbstractStrategy e formaliza
    todos os comportamentos no âmbito do cálculo do Valor Futuro.
    """

    def calculate_steps(simulation_investment):

        """Método que preenche uma lista com o 
        resultado de cada iteração do cálculo de
        Valor Futuro.
        """

        result = pv = simulation_investment.present_value
        period = simulation_investment.period_value
        rate = simulation_investment.rate_value/100
        result_list = [pv]
        for k in range(1, period):
            result += (result*rate)
            result_list.append(result)
        return result_list

    def validate_result(simulation_investment,result):

        """Método que verifica se último valor da iteração
        de cálculos do Valor Futuro condiz com a aplicação
        direta da equação para o período fornecido.
        """

        pv = simulation_investment.present_value
        period = simulation_investment.period_value
        rate = simulation_investment.rate_value/100
        return pv*((1 + rate)**period) == result


class PayBackStrategy(SimulationAbstractStrategy):

    """Classe PayBackStrategy. Classe que realiza 
    extensão da Classe SimulationAbstractStrategy e formaliza
    todos os comportamentos no âmbito do cálculo do PayBack.
    """

    def calculate_steps(simulation_investment):
    	pv = simulation_investment.present_value
    	pmt = simulation_investment.payment_value
    	result_list = [pv/pmt]
    	pv -= pmt
    	while pv > 0:
    		result_list.append(pv/pmt)
    		pv -= pmt
    	return result_list

    def validate_result(simulation_investment,result):

        """Método que implementa o cálculo direto para
        a verificação do PayBack simples para um determinado
        investimento.
        """

        pv = simulation_investment.present_value
        pmt = simulation_investment.payment_value
        return pv/pmt == result


class Category(models.Model):

    """Classe Category. Classe que possui as informações inerentes
    ao mantenimento de categorias de receitas e despesas.
    """

    # Name of category recorded
    # Name of category never should be blank
    category_name = models.CharField(_('Name Category'), max_length=30, blank=False)

    # Detail of category recorded
    # Is not required
    category_description = models.TextField(_('Description Category'), max_length=150, blank=True)

    # Tipos de Lancamento
    INCOME = _('Income')
    EXPENSE = _('Expense')

    # Enum de Lancamentos
    ENTRY_TYPE = (
    (INCOME, _('Income')),
    (EXPENSE, _('Expense')),
    )

    def __str__(self):

        """Método de conversão para
        o formato string.
        """

        return self.category_name

class Entry(models.Model):

    """Classe Entry. Classe que possui as informações detalhadas
    de um determinado lançamento, podendo ser receita ou despesa.
    """

    # Empresa/Organizacao/Entidade fonte da requisicao do Lancamento
    entry_source = models.CharField(_('Entry Source'), max_length=50, blank=True)

    # Registro do Valor do Lancamento
    entry_value = models.DecimalField(_('Entry Value'), decimal_places=2, max_digits=12)
    
    # Data de Vencimento
    entry_due_date = models.DateField(_('Due Date'))

    # Data de Registro do Lancamento
    entry_registration_date = models.DateField(_('Registration Date'))

    # Descricao do Lancamento
    entry_description = models.TextField(_('Entry Description'), max_length=150, blank=True)

    # Quantidade de Parcelas
    entry_quota_amount = models.PositiveIntegerField(_('Entry Quota Amount'), default=1)

    # Tipo de Periodicidade do Lancamento
    entry_periodicity = models.CharField(_('Entry Periodicity Type'), choices=Finance.PERIODICITY, default=Finance.MONTHLY, max_length=20)
    
    # Tipo do Lancamento
    entry_type = models.CharField(_('Entry Type'), choices=Category.ENTRY_TYPE, default=Category.EXPENSE, max_length=20)

    # Relacionamento de 1 pra n com Categoria de lancamento
    category = models.ForeignKey(Category, verbose_name=_('Entry Category'))

    # Relacionamento de 1 pra n com Usuario
    entry_user = models.ForeignKey(User, verbose_name=_('User'))

    # Valores Possiveis de Estado de Valor e Parcela
    OVERDUE = _('Overdue')
    NO_OVERDUE = _('No Overdue Yet')
    ALL_ENTRY = _('All Entry')

    # Enum de Estado de um Valor
    VALUE_STATE = (
        (OVERDUE, _('Overdue')),
        (NO_OVERDUE, _('No Overdue Yet')),
        (ALL_ENTRY, _('All Entry')),
    )

    # Enum de Estado de uma Parcela
    QUOTA_STATE = (
        (OVERDUE, _('Overdue')),
        (NO_OVERDUE, _('No Overdue Yet')),
    )

    def __str__(self):

        """Método de conversão para
        o formato string.
        """

        return self.entry_description