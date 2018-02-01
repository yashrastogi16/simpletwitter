# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import TweetForm

# Create your views here.

class TweetView(FormView):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(TweetView, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		content = {}
		content['form'] = TweetForm
		return render_to_response('tweet.html', content, {})

	def post(self, request, *args, **kwargs):
		content = {}
		form = TweetForm(request.POST, request.FILES or None)
		if form.is_valid():
			tweetobj = form.save()
			user = request.user
			user.tweet.add(tweetobj)
			user.save()
			return redirect(reverse('dashboard-view'))
			template = 'tweet.html'
			return render_to_response(template, content)