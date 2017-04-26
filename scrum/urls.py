from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /portfolio
    #url(r'^portfolio', views.portfolio, name='portfolio'),

    # ex: /portfolio/5/
    url(r'^(?P<statusId>[0-9]+)/$', views.portfolio, name='portfolio'),
]