from django import forms

from organisations.models import Booking


class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booked_at', 'email', 'phone')