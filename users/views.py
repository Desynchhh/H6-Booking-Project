from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, FormView
from access_rules import UserIsOrganisationLeaderMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.contrib import messages

from .models import Profile, Role
from .forms import UserRegisterForm
from organisations.models import Organisation
from organisations.forms import OrganisationRegisterForm

# Create your views here.
class RegisterFormView(LoginRequiredMixin, UserIsOrganisationLeaderMixin, FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm

    def get_success_url(self):
        organisation = self.request.user.profile.organisation
        kwargs = {
            'pk': organisation.id,
            'slug': organisation.slug
        }
        return reverse('organisations:detail', kwargs=kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            user.profile.role = Role.objects.get(name='Employee')
            user.profile.organisation = self.request.user.profile.organisation
            user.profile.save()
            return redirect(self.get_success_url())
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['organisation_id'] = self.request.user.profile.organisation.id
        return initial
