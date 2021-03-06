from django.conf.urls import url
#from . import views
from scrum.views.portfolioView import *
from scrum.views.portfolioView import PortfolioListbyStatus, PortfolioList, PortfolioDetails, PortfolioCreate, PortfolioUpdate, PortfolioDelete
from scrum.views.releaseView import ReleaseList, ReleaseCreate, ReleaseDetails, ReleaseDelete, ReleaseUpdate
from scrum.views.releaseView import UserstoryDetails, UserstoryCreate, UserstoryUpdate, UserstoryDelete
from scrum.views.releaseView import TaskCreate, TaskUpdate, TaskDelete
from scrum.views.releaseView import SprintDetails, SprintCreate, SprintUpdate, SprintDelete
from scrum.views.teamview import TeamList, TeamCreate, TeamUpdate, TeamDetails, TeamDelete
from scrum.views.teamview import TeamResourceCreate, TeamResourceUpdate, TeamResourceDelete
app_name = 'scrum'
urlpatterns = [
    url(r'^$',  PortfolioList.as_view(), name='index'),
    #url(r'^dashboard', Dashboard.as_view(), name='dashboard'),
    url(r'^portfolio/list/(?P<status_id>\d+)$',  PortfolioListbyStatus.as_view(), name='portfolioListbyStatus'),
    url(r'^portfolio/list', PortfolioList.as_view(), name='portfolioList'),
    url(r'^portfolio/(?P<pk>\d+)$', PortfolioDetails.as_view(), name='portfolio-detail'),
    url(r'^portfolio/add', PortfolioCreate.as_view(), name='portfolio-add'),
    url(r'^portfolio/update/(?P<pk>\d+)$', PortfolioUpdate.as_view(), name='portfolio-update'),
    url(r'^portfolio/delete/(?P<pk>\d+)$', PortfolioDelete.as_view(), name='portfolio-delete'),
    # release Release
    url(r'^releaseList',  ReleaseList.as_view(), name='releaseList'),
    url(r'^release/(?P<pk>\d+)$', ReleaseDetails.as_view(), name='release-detail'),
    url(r'^release/add/(?P<portfolio_id>\d+)$', ReleaseCreate.as_view(), name='release-add'),
    url(r'^release/update/(?P<pk>\d+)$', ReleaseUpdate.as_view(), name='release-update'),
    url(r'^release/delete/(?P<pk>\d+)$', ReleaseDelete.as_view(), name='release-delete'),
    # Userstory, userstory
    #url(r'^releaseList', ReleaseList.as_view(), name='releaseList'),
    url(r'^Userstory/(?P<pk>\d+)$', UserstoryDetails.as_view(), name='userstory-detail'),
    url(r'^Userstory/add/(?P<release_id>\d+)$',UserstoryCreate.as_view(), name='userstory-add'),
    url(r'^Userstory/update/(?P<pk>\d+)$',UserstoryUpdate.as_view(), name='userstory-update'),
    url(r'^Userstory/delete/(?P<pk>\d+)$', UserstoryDelete.as_view(), name='userstory-delete'),

    # Task, task
    #url(r'^Task/(?P<pk>\d+)$', TaskDetails.as_view(), name='userstory-detail'),
    url(r'^Task/add/(?P<userstory_id>\d+)$', TaskCreate.as_view(), name='task-add'),
    url(r'^Task/update/(?P<pk>\d+)$', TaskUpdate.as_view(), name='task-update'),
    url(r'^Task/delete/(?P<pk>\d+)$', TaskDelete.as_view(), name='task-delete'),
    # Sprint, sprint
    # release Release
    # not needed now may be later:
    # url(r'^sprintList', SprintList.as_view(), name='releaseList'),
    # not needed now may be later:
    url(r'^sprint/(?P<pk>\d+)$', SprintDetails.as_view(), name='sprint-detail'),
    url(r'^sprint/add/(?P<release_id>\d+)$', SprintCreate.as_view(), name='sprint-add'),
    url(r'^sprint/update/(?P<pk>\d+)$', SprintUpdate.as_view(), name='sprint-update'),
    url(r'^sprint/delete/(?P<pk>\d+)$', SprintDelete.as_view(), name='sprint-delete'),
    #url(r'^sprint/userstory-select/(?P<pk>\d+)$', Sprint_userstorySelect.as_view(), name='sprint-userstory-select'),
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

    # Team, team
    url(r'^team/list', TeamList.as_view(), name='team-list'),
    url(r'^team/(?P<pk>\d+)$', TeamDetails.as_view(), name='team-detail'),
    url(r'^team/add', TeamCreate.as_view(), name='team-add'),
    url(r'^team/update/(?P<pk>\d+)$', TeamUpdate.as_view(), name='team-update'),
    url(r'^team/delete/(?P<pk>\d+)$', TeamDelete.as_view(), name='team-delete'),
    url(r'^teamresource/add', TeamResourceCreate.as_view(), name='teamresource-add'),
    url(r'^teamresource/update/(?P<pk>[\w\-]+)$', TeamResourceUpdate.as_view(), name='teamresource-update'),
    url(r'^teamresource/delete/(?P<pk>[\w\-]+)$', TeamResourceDelete.as_view(), name='teamresource-delete'),
]

