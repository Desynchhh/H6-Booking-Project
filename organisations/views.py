from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from users.forms import UserRegisterForm
from .forms import OrganisationRegisterForm
from .models import Organisation
from users.models import Role

from access_rules import (
    UserInOrganisationMixin
)

# Create your views here.
class OrganisationDetailView(LoginRequiredMixin, UserInOrganisationMixin, DetailView):
    model = Organisation


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
