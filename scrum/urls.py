from django.conf.urls import url
#from . import views
from scrum.views.portfolioView import *
from scrum.views.portfolioView import PortfolioList, PortfolioDetails, PortfolioCreate, PortfolioUpdate, PortfolioDelete
app_name = 'scrum'
urlpatterns = [
    url(r'^$',  PortfolioList.as_view(), name='index'),
    url(r'^dashboard', Dashboard.as_view(), name='dashboard'),
    url(r'^portfolioList',  PortfolioList.as_view(), name='portfolioList'),
    url(r'^portfolio/(?P<pk>\d+)$', PortfolioDetails.as_view(), name='portfolio-detail'),
    url(r'^portfolio/add', PortfolioCreate.as_view(), name='portfolio-add'),
    url(r'^portfolio/update/(?P<pk>\d+)$', PortfolioUpdate.as_view(), name='portfolio-update'),
    url(r'^portfolio/delete/(?P<pk>\d+)$', PortfolioDelete.as_view(), name='portfolio-delete'),

    # url(r'^portfolio/Details/(?P<id>\d+)/$', portfolioDetails(), name='portfolioDetails'),
   # url(r'^portfolio/Update/(?P<id>\d+)/$', portfolios.portfolioUpdate, name='portfolioUpdate'),
   # url(r'^portfolio/Update', portfolios.portfolioUpdate, name='portfolioUpdate'),
   # url(r'^portfolio/new$', portfolios.new_portfolio, name='new_portfolio'),
   # url(r'^portfolio', portfolios.portfolio, name='portfolio'),
   # url(r'^userstoryList', userstories.,
    #url(r'^release/(?P<id>\d+)/$', portfolios.releaseUpdate, name='releaseUpdate'),
   # url(r'^release/new$', userstories.new_userstory, name='new_release'),
   # url(r'^userstory/new$', userstories.new_userstory, name='new_userstory'),
    #url(r'^sprint/new$', views.new_sprint, name='new_sprint'),
    #url(r'^task/new$', views.new_task, name='new_task'),
    #url(r'^team/new$', views.new_team, name='new_release'),
]
