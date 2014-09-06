from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.layout import Submit, Reset
from crispy_forms.helper import FormHelper


class SearchForm(forms.Form):
    first_name = forms.CharField(max_length=50, label=_('Nombre'))
    last_name = forms.CharField(max_length=50, label=_('Apellido'))
    email = forms.EmailField()
    address = forms.CharField(max_length=400, label=_('Dirección'))
    dni = forms.IntegerField(label='DNI')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'col-lg-7'
        self.helper.add_input(Submit('submit', _('Buscar')))
        self.helper.add_input(Reset('job_reset', _('Limpiar'),
                                    css_class='btn-default'))
