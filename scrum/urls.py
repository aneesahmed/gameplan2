from django.conf.urls import url
from . import views

app_name = 'scrum'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^portfolio/Details/(?P<id>\d+)/$', views.portfolioDetails, name='portfolioDetails'),
    url(r'^portfolio/Update/(?P<id>\d+)/$', views.portfolioUpdate, name='portfolioUpdate'),
    url(r'^portfolio/Update', views.portfolioUpdate, name='portfolioUpdate'),
    url(r'^portfolio/new$', views.new_portfolio, name='new_portfolio'),
    url(r'^portfolio', views.portfolio, name='portfolio'),
    url(r'^release/(?P<id>\d+)/$', views.releaseUpdate, name='releaseUpdate'),
    url(r'^release/new$', views.new_release, name='new_release'),
    url(r'^userstory/new$', views.new_userstory, name='new_userstory'),
    #url(r'^sprint/new$', views.new_sprint, name='new_sprint'),
    #url(r'^task/new$', views.new_task, name='new_task'),
    #url(r'^team/new$', views.new_team, name='new_release'),
]

# User Story, userstory
'''
url(r'^userstory/new$', views.new_userstory, name='new_userstory'),
url(r'^userstory', views.userstory, name='userstory'),
# sprint
url(r'^sprint/(?P<id>\d+)/$', views.sprintUpdate, name='sprintUpdate'),
url(r'^sprint/new$', views.new_sprint, name='new_sprint'),
url(r'^sprint', views.portfolio, name='sprint'),
# Task, task
url(r'^task/(?P<id>\d+)/$', views.taskUpdate, name='taskUpdate'),
url(r'^task/new$', views.new_task, name='new_task'),
# Team , team
url(r'^team/(?P<id>\d+)/$', views.teamUpdate, name='teamUpdate'),
url(r'^team/new$', views.new_team, name='new_team'),

#Retro meeting
'''