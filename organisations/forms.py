from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext as _
from .models import Organisation, OpeningHour


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


# DAY_CHOICES = (
#     ('', '----'),
#     (0, 'Mandag'),
#     (1, 'Tirsdag'),
#     (2, 'Onsdag'),
#     (3, 'Torsdag'),
#     (4, 'Fredag'),
#     (5, 'Lørdag'),
#     (6, 'Søndag'),
# )

class OpeningHourCreateForm(forms.ModelForm):
    day = forms.ChoiceField(choices=OpeningHour.DayChoices.choices)
    day.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = OpeningHour
        fields = ('day', 'time_open', 'working_time')

        widgets = {
            'time_open': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eks. 08:15'}),
            'working_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eks. 16:00' }),
        }


class OpeningHourDeleteForm(forms.ModelForm):
    day = forms.ChoiceField(choices=OpeningHour.DayChoices.choices)
    day.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = OpeningHour
        fields = ('day', 'time_open')

        widgets = {
            'time_open': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eks. 08:15'}),
        }
