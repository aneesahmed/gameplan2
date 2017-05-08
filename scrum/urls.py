from django.conf.urls import url
from . import views

app_name = 'scrum'
urlpatterns = [
    # page for adding a new portfolio
    url(r'^newPortfolio/$', views.newPortfolio, name='new_topic'),
    url(r'^portfolioDashboard', views.portfolioDashboard, name='portfolio'),
    #
    url(r'^portfolio/(?P<id>[0-9]+)/$', views.newPortfolio, name='portfolio'),
    #portfolio/0-99

    #url(r'^portfolio/(?P<id>[0-9]+)/$', views.portfolioForm, name='portfolio'),
    # ex: /portfolio/5/
    url(r'^$', views.portfolioDashboard, name='portfolio'),     
] 