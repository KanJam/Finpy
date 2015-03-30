from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from Finpy.models import UserProfile
from Finpy.forms import UserCreationForm, ProfileUpdateForm

# Create your views here.

@login_required
def index(request, template_name='Finpy/index.html'):
    context = {
        'profile_id': request.user.userprofile.id,
        'title': _('Home'),
    }
    return TemplateResponse(request, template_name, context)

@login_required
def update_profile(request, profile_id=None, template_name='profile/update.html',
    update_form=ProfileUpdateForm, current_app=None, extra_context=None):

    if profile_id is not None:
        profile = UserProfile.objects.get(pk=int(profile_id))
        user = profile.user
        if user == request.user:
            if request.method == "POST":
                form = update_form(data=request.POST, instance=profile)
                if form.is_valid():
                    form.save()
            else:
                form = update_form(instance=profile)

            context = {
                'form': form,
                'title': _('User Profile Update'),
            }
            if extra_context is not None:
                context.update(extra_context)
            return TemplateResponse(request, template_name, context,
                current_app=current_app)
        else:
            return HttpResponse(_("This isn't your profile"))

def signup(request, template_name='registration/signup.html',
    post_signup_redirect=None, signup_form=UserCreationForm,
    current_app=None, extra_context=None):
    if post_signup_redirect is None:
        post_signup_redirect = reverse('login')
    else:
        post_signup_redirect = resolve_url(post_signup_redirect)
    if request.method == "POST":
        form = signup_form(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile()
            profile.user = user
            profile.save()
            return HttpResponseRedirect(post_signup_redirect)
    else:
        form = signup_form()
    context = {
        'form': form,
        'title': _('User Registration'),
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
        current_app=current_app)
