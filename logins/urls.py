from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
	url(r'^$', views.base),
	url(r'^login/$', views.login, name='login'),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'postsignin/$', views.postsignin),
	url(r'postlogin/$', views.postlogin),
]
