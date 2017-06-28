from django.conf.urls import url

from . import views

app_name = 'codesample'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uploadfile/$', views.uploadfile, name='uploadfile'),
    url(r'^downloadsamplefile/$', views.downloadsamplefile, name='downloadsamplefile'),
]
