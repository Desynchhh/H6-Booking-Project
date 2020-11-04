from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext as _
from .models import Organisation


class OrganisationRegisterForm(forms.ModelForm):
    phone = forms.IntegerField(required=False)

    def clean(self):
        phone = self.cleaned_data.get('phone')
        if len(str(phone)) != 8:
            raise ValidationError(_('Indtast et gyldigt telefon nummer'))
        return self.cleaned_data

    class Meta:
        model = Organisation
        fields = ('name', 'address', 'phone')
