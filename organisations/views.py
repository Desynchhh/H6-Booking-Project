from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Organisation
from access_rules import (
    UserInOrganisationMixin
)

# Create your views here.
class OrganisationDetailView(LoginRequiredMixin, UserInOrganisationMixin, DetailView):
    model = Organisation
