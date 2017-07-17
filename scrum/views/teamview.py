# coding=utf-8
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from  scrum.models import PortfolioStatus, Portfolio, PortfolioReleases, Userstory,ReleaseStatus, Sprint
from scrum.models import Team, TeamResource
from django.template import loader
from django.urls import reverse_lazy,reverse
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from scrum.forms import ReleaseForm, UserstoryForm, SprintForm
from django import forms


class TeamList(LoginRequiredMixin,ListView):
    model = Team
    template_name = 'scrum/team_list.html'
    context_object_name = 'teamlist'
    paginate_by = 20


class TeamDetails(LoginRequiredMixin,DetailView):
    model = Team
    template_name = 'scrum/teamDetails.html'
    context_object_name = 'team'

    #def get_context_data(self, *args, **kwargs):
    #    context = super(TeamDetails, self).get_context_data(*args, **kwargs)
    #    context['statuses'] = ReleaseStatus.objects.all()
    #    return context

class TeamDetailsbyStatus(LoginRequiredMixin, DetailView):
    model = Team
    template_name = 'scrum/portfolioDetails.html'
    context_object_name = 'portfolio'


    def get_queryset(self):
        status = int(self.kwargs['status_id'])
        if (status>0):
            return PortfolioReleases.objects.all().filter(releasestatusid_id=status)
        else:
            return PortfolioReleases.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TeamDetailsbyStatus, self).get_context_data(*args, **kwargs)
        #context['portfolioreleases_set']
        context['statuses'] = ReleaseStatus.objects.all()
        return context

class TeamCreate(LoginRequiredMixin,CreateView):
    model = Team
    fields =  ['title' ]

    success_url = reverse_lazy('scrum:team-list')

    #def form_valid(self, form):
    #        form.instance.createby = self.request.user.username
    #        return super(PortfolioCreate, self).form_valid(form)

class TeamUpdate(LoginRequiredMixin,UpdateView):
    model = Team
    fields = ['title']
    #fields =  ['title','portfoliotypeid','owner','details','rank','portfoliostatusid' ]
    #def form_valid(self, form):
            #form.instance.portfolioId
     #       form.instance.updateby =  self.request.user.username
            #form.instance.portfolioid = Portfolio.objects.get(pk=self.kwargs['portfolio_id'])
    #        return super(Team, self).form_valid(form)
    success_url = reverse_lazy('scrum:team-list')

class TeamDelete(LoginRequiredMixin,DeleteView):
    model = Team
    success_url = reverse_lazy('scrum:team-list')

##### TeamResource teamresource

class TeamResourceCreate(LoginRequiredMixin,CreateView):
    model = TeamResource
    fields = ['resourceid', 'name', 'title' ,'teamid']

    success_url = reverse_lazy('scrum:team-list')

    #def form_valid(self, form):
    #        form.instance.createby = self.request.user.username
    #        return super(PortfolioCreate, self).form_valid(form)

class TeamResourceUpdate(LoginRequiredMixin,UpdateView):
    model = TeamResource
    fields = ['resourceid', 'name', 'title' ,'teamid']
    #fields =  ['title','portfoliotypeid','owner','details','rank','portfoliostatusid' ]
    #def form_valid(self, form):
            #form.instance.portfolioId
     #       form.instance.updateby =  self.request.user.username
            #form.instance.portfolioid = Portfolio.objects.get(pk=self.kwargs['portfolio_id'])
    #        return super(Team, self).form_valid(form)
    success_url = reverse_lazy('scrum:team-list')

class TeamResourceDelete(LoginRequiredMixin,DeleteView):
    model = TeamResource
    success_url = reverse_lazy('scrum:team-list')