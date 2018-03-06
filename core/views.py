# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import LoginForm, RegisterForm

from django.shortcuts import render_to_response, HttpResponseRedirect, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from .models import User

# Create your views here.


def base(request):
    return render_to_response('base.html')


def home(request):
    return render_to_response('home.html')


class RegisterView(FormView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        content = {}
        content['form'] = RegisterForm
        if request.user.is_authenticated():
            return redirect(reverse('dashboard-view'))
        return render_to_response('register.html', content, {})

    def post(self, request, *args, **kwargs):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.password = make_password(form.cleaned_data['password'])
            save_it.save()
            login(request, save_it)
            return redirect(reverse('dashboard-view'))
            template = 'register.html'
            return render_to_response(template, content)


class LoginView(FormView):

    content = {}
    content['form'] = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('dashboard-view'))
        content = {}
        content['form'] = LoginForm
        return render_to_response('login.html', content, {})

    def post(self, request):
        content = {}
        email = request.POST['email']
        password = request.POST['password']
        try:
            users = User.objects.filter(email=email)
            user = authenticate(request, username=users.first().username, password=password)
            login(request, user)
            return redirect(reverse('dashboard-view'))
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Unable to login with provided credentials' + e
            return render_to_response('login.html', content)


class DashboardView(FormView):

    def get(self, request):

        content = {}
        if request.user:
            user = request.user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            content['userdetail'] = user
            content['following'] = User.objects.filter(follower=request.user)
            return render_to_response('dashboard.html', content)
        else:
            return redirect(reverse('login-view'))


class LogoutView(FormView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
