from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from Finpy.models import UserProfile, Entry, InvestmentSimulation

class UserCreationForm(forms.ModelForm):
    
    """Classe UserCreationForm. Classe que possui
    os tratamentos inerentes à lógica dos formulários
    existentes na página de criação de usuário.
    """

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:

        """Classe Meta. Classe que define as informações
        que serão utilizadas com base no conjunto já existente
        da Model User do framework Django.
        """

        model = User
        fields = ("username","first_name","last_name","email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class InvestmentSimulationForm(forms.ModelForm):

    """Classe InvestmentSimulationForm. Classe que possui
    os tratamentos inerentes à lógica dos formulários
    existentes na página de preenchimento de informações
    para a simulação de investimento.
    """

    class Meta:

        """Classe Meta. Classe que define as informações
        que serão utilizadas com base no conjunto existente
        na Model InvestmentSimulation.
        """

        model = InvestmentSimulation
        fields = '__all__'
        exclude = ['simulation_user']

class ProfileUpdateForm(forms.ModelForm):

    """Classe ProfileUpdateForm. Classe que possui
    os tratamentos inerentes à lógica dos formulários
    existentes na página de atualização das informações
    do usuário.
    """

    class Meta:

        """Classe Meta. Classe que define as informações
        que serão utilizadas com base no conjunto já existente
        da Model UserProfile.
        """

        model = UserProfile
        fields = '__all__'
        exclude = ['user',]

class EntryForm(forms.ModelForm):

    """Classe EntryForm. Classe que possui
    os tratamentos inerentes à lógica dos formulários
    existentes na página de inserção de lançamentos
    de receitas e despesas.
    """

    class Meta:

        """Classe Meta. Classe que define as informações
        que serão utilizadas com base no conjunto já existente
        da Model Entry.
        """

        model = Entry
        fields = '__all__'
        exclude = ['entry_user']

    def delete(self, instance=None):
        return instance.delete()
