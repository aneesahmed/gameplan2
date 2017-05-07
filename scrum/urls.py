from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.portfolio, name='portfolio'),

    url(r'^portfolio/add', views.portfolioAdd, name='portfolioadd'),
    # ex: /portfolio
    url(r'^portfolio', views.portfolio, name='portfolio'),

    # ex: /portfolio/5/
    
] 