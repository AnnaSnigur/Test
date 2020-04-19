# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from profile_app.forms import SignUpForm, EditForm
from profile_app.models import Profile
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy


class MyProfile(UpdateView):
    template_name = 'home.html'
    queryset = Profile.objects.filter(is_active=True)
    success_url = reverse_lazy('index')


class SignUp(CreateView):
    template_name = 'signup.html'
    queryset = Profile.objects.all()
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class EditProfile(UpdateView):
    template_name = 'edit.html'
    queryset = Profile.objects.filter(is_active=True)
    success_url = reverse_lazy('index')
    form_class = EditForm


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Login(ListView):
    model = Profile
    fields = ['username', 'password']
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
