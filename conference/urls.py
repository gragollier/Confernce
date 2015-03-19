from django.conf.urls import patterns, url

from conference import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^teacher_redirect', views.teacher_redirect, name='teacher_redirect'),
                       url(r'^teacher', views.TeacherView.as_view(), name='teacher'),
                       url(r'^(?P<pk>\d+)/time/$', views.TimeView.as_view(), name='time'),
                       url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),
                       # Vote is used because I didn't have a better idea
)