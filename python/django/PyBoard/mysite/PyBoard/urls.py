from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<topic_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<topic_id>\d+)/reply/$', views.reply, name='reply'),
]
