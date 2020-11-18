from django.shortcuts import render
from django.views.generic import ListView, DetailView

from organisations.models import Organisation, OpeningHour

from datetime import time

# Create your views here.

def temp_home(request):
    return render(request, 'booking/temp_home.html', context={"my_name": "Mikkel Larsen"})

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
        context['table_hours'] = [int(f'{x:02}') for x in range(0, 24, 1)]
        context['table_minutes'] = [int(f'{x:02}') for x in range(0, 60, 15)]
        table_times = {}
        for minute in context['table_minutes']:
            table_times[minute] = {}
            for hour in context['table_hours']:
                table_times[minute][hour] = {'time': time(hour, minute)}
        for k, v in table_times.items():
            for t, i in table_times[k].items():
                print(t)
        # test = time(hour=context['table_hours'][0], minute=context['table_minutes'][0])
        # print(context['opening_hours']['MONDAY'][0].get_closing_hours)
        # print(context['opening_hours']['MONDAY'][0].time_open > test)
        return context
    