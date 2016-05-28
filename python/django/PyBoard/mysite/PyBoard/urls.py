from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    #url(r'^contact/$', views.contact, name='contact'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<topic_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<topic_id>\d+)/reply/(?P<text_no>\d+)/$', views.reply, name='reply'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^signup/$', views.signup, name='signup'),
]
