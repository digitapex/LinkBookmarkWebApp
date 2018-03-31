"""FirstAppDjango URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from posts.views import show_post
from posts.views import delete, add_page, edit, sort, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', show_post, name='show_post'),
    # url(r'^new$', new, name='new'),
    url(r'^add_page', add_page, name='add_page'),
    url(r'^edit/(?P<pk>\d+)$', edit, name='edit'),
    url(r'^delete/(?P<pk>\d+)$', delete, name='delete'),
    url(r'^sort/$', sort, name='sort'),
    url(r'^login/$', auth_views.login, {'template_name': 'posts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]
