from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin


class UserPassesTestHandler(UserPassesTestMixin):
    def handle_no_permission(self):
        return redirect('login')


class UserInOrganisationMixin(UserPassesTestHandler):
    def test_func(self):
        current_organisation = self.get_object()
        return self.request.user.profile.organisation == current_organisation
