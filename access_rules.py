from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin

from organisations.models import Organisation, OpeningHour


class UserPassesTestHandler(UserPassesTestMixin):
    def handle_no_permission(self):
        return redirect('login')


class UserInOrganisationMixin(UserPassesTestHandler):
    def test_func(self):
        organisation = self.get_object()
        return self.request.user.profile.organisation == organisation


class UserIsOrganisationLeaderMixin(UserPassesTestHandler):
    def test_func(self):
        organisation = get_object_or_404(Organisation, pk = self.kwargs['pk'], slug = self.kwargs['slug'])
        profile = self.request.user.profile
        return profile.organisation == organisation and profile.role.name == 'Leader'


class UserIsOpeningHourLeaderMixin(UserPassesTestHandler):
    def test_func(self):
        oh = get_object_or_404(OpeningHour, pk=self.kwargs['org_id'])
        organisation = oh.organisation
        profile = self.request.user.profile
        return profile.organisation == organisation and profile.role.name == 'Leader'
