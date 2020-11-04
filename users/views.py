from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView

from django.contrib import messages

from .forms import UserRegisterForm
from organisations.forms import OrganisationRegisterForm

# Create your views here.
class RegisterTemplateView(TemplateView):
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('login')

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        u_form = UserRegisterForm(request.POST)
        o_form = OrganisationRegisterForm(request.POST)
        if o_form.is_valid() and u_form.is_valid():
            organ = o_form.save()
            user = u_form.save()
            user.profile.organisation = organ
            user.profile.save()
            messages.success(self.request, 'Account created successfully.')
            return redirect(reverse('login', kwargs=kwargs))
        messages.error(self.request, 'Account was not created.')
        context['forms'] = {
            'u_form': UserRegisterForm(),
            'o_form': OrganisationRegisterForm()
        }
        return super().render_to_response(context, **kwargs)


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['forms'] = {
            'u_form': UserRegisterForm(),
            'o_form': OrganisationRegisterForm()
        }
        return context


def register(request):
    if request.method == 'POST':
        o_form = OrganisationRegisterForm(request.POST)
        u_form = UserRegisterForm(request.POST)
        if o_form.is_valid() and u_form.is_valid():
            organ = o_form.save()
            user = u_form.save()
            user.profile.organisation = organ
            user.profile.save()
            messages.success(request, 'Account created successfully.')
            return redirect(request, 'users/login')
    else:
        o_form = OrganisationRegisterForm()
        u_form = UserRegisterForm()
    context = {
        'forms': {
            'u_form': u_form,
            'o_form': o_form,
        }
    }
    return render(request, 'users/register.html', context=context)
