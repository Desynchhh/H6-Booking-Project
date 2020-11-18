from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, FormView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from users.forms import UserRegisterForm
from .forms import OrganisationRegisterForm, OpeningHourCreateForm
from .models import Organisation, OpeningHour
from users.models import Role

from access_rules import (
    UserInOrganisationMixin,
    UserIsOrganisationLeaderMixin,
    UserIsOpeningHourLeaderMixin
)

import datetime

# Create your views here.
class OrganisationDetailView(LoginRequiredMixin, UserInOrganisationMixin, DetailView):
    model = Organisation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        opening_hours = OpeningHour.objects.filter(organisation=context['organisation'])
        context['opening_hours'] = {}
        for day in OpeningHour.DayChoices:
            context['opening_hours'][day.name] = opening_hours.filter(day=day)
        return context
    


def register(request):
    if request.method == 'POST':
        o_form = OrganisationRegisterForm(request.POST)
        u_form = UserRegisterForm(request.POST)
        if o_form.is_valid() and u_form.is_valid():
            roles = Role.objects.get_all_roles()
            organ = o_form.save()
            user = u_form.save()
            user.profile.organisation = organ
            user.profile.role = roles.get(name='Leader')
            user.profile.save()
            messages.success(request, 'Account created successfully.')
            return redirect(reverse('login'))
    else:
        o_form = OrganisationRegisterForm()
        u_form = UserRegisterForm()
    context = {
        'forms': {
            'u_form': u_form,
            'o_form': o_form,
        }
    }
    return render(request, 'organisations/register.html', context=context)



class CreateOpeningFormView(LoginRequiredMixin, UserIsOrganisationLeaderMixin, FormView):
    template_name = 'organisations/openinghour_create.html'
    form_class = OpeningHourCreateForm
    
    def get_success_url(self):
        return reverse('organisations:opening-hours-create', kwargs={'pk': self.kwargs.get('pk'), 'slug': self.kwargs.get('slug')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        opening_hours = OpeningHour.objects.filter(organisation__id=self.kwargs.get('pk'))
        context['opening_hours'] = {}
        for day in OpeningHour.DayChoices:
            context['opening_hours'][day.name] = opening_hours.filter(day=day).order_by('time_open')
        return context
    
    def form_valid(self, form):
        time_open = str(form.cleaned_data["time_open"])
        time_open_hours, time_open_minutes, *_ = time_open.split(':')
        time_open_delta = datetime.timedelta(hours=int(time_open_hours), minutes=int(time_open_minutes))

        working_time = str(form.cleaned_data["working_time"])
        working_hours, working_minutes, *_ = working_time.split(':')
        working_time_delta = datetime.timedelta(hours=int(working_hours), minutes=int(working_minutes))

        time_diff = working_time_delta - time_open_delta
        
        self.object = form.save(commit=False)
        self.object.organisation = Organisation.objects.get(pk=self.kwargs.get('pk'))
        self.object.working_time = int(time_diff.total_seconds()/60)
        self.object.save()
        return redirect(self.get_success_url())


class OpeningHourDeleteView(LoginRequiredMixin, UserIsOpeningHourLeaderMixin, DeleteView):
    model = OpeningHour

    def get_success_url(self):
        return reverse('organisations:opening-hours-create', kwargs={'pk': self.kwargs.get('org_id'), 'slug': self.kwargs.get('slug')})
