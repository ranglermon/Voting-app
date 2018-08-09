from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^createuser/$', views.create_user, name='create_user'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/create_election/$', views.get_election_id, name='createelection'),
    url(r'^dashboard/edit_election/(?P<election>[\w\-]+)/$', views.create_election, name='election'),

    ]
