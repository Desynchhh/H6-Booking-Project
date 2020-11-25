from django.shortcuts import render
from django.views.generic import ListView, DetailView

from organisations.models import Organisation, OpeningHour

from datetime import time

# Create your views here.

class OrganisationListView(ListView):
    model = Organisation
    template_name = 'booking/organisation_list.html'


class OrganisationDetailView(DetailView):
    model = Organisation
    template_name = 'booking/organisation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        opening_hours = OpeningHour.objects.filter(organisation=context['object'])
        context['opening_hours'] = {}
        for day in OpeningHour.DayChoices:
            context['opening_hours'][day.name] = opening_hours.filter(day=day)
        context['table_hours'] = [str(x).zfill(2) for x in range(0, 24, 1)]
        context['table_minutes'] = [str(x).zfill(2) for x in range(0, 60, 15)]
        return context
    