"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from login.views import *

import contacts.views
urlpatterns = patterns('',
	url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^viewsub$', contacts.views.ListContactView.as_view(),
	name='contacts-list',),
	url(r'^submission$', submission),
        url(r'^logout/$', logout_page),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
	url(r'^register/$', register, name='register'),
	url(r'^register/success/$', register_success),
	url(r'^home/$', home),
	url(r'^new$', contacts.views.CreateContactView.as_view(),
	name='contacts-new',),
	url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(),
	name='contacts-edit',),
	url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(),
	name='contacts-delete',),
	url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(),
	name='contacts-view',),
)
