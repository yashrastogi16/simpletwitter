"""twittersimple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from core.views import base, LoginView, home, DashboardView, RegisterView, LogoutView
from twitter.views import TweetView, FollowView, UnFollowView, FavouriteView, UnFavouriteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base/', base, name='base'),
    url(r'^$', home, name='home'),
    url(r'^login/', LoginView.as_view(), name='login-view'),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard-view'),
    url(r'^register/', RegisterView.as_view(), name='register-view'),
    url(r'^tweet/', TweetView.as_view(), name='tweet-view'),
    url(r'^follow/$', FollowView.as_view(), name='follow-view'),
    url(r'^follow/(?P<pk>[0-9]+)/$', FollowView.as_view(), name='follow-view'),
    url(r'^unfollow/(?P<pk>[0-9]+)/$', UnFollowView.as_view(), name='unfollow-view'),
    url(r'^favourite/(?P<pk>[0-9]+)/$', FavouriteView.as_view(), name='favourite-view'),
    url(r'^unfavourite/(?P<pk>[0-9]+)/$', UnFavouriteView.as_view(), name='unfavourite-view'),
    url(r'logout/$', LogoutView.as_view(), name='logout-view'),
]
