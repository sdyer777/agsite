from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^polls/', include('codesample.urls')),
    url(r'^$', views.index, name='index'),
]
