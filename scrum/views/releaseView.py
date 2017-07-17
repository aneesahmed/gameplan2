from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from  scrum.models import PortfolioStatus, Portfolio, PortfolioReleases, Userstory,ReleaseStatus, Sprint,Task, TaskStatus
from django.template import loader
from django.urls import reverse_lazy,reverse
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from scrum.forms import ReleaseForm, UserstoryForm, SprintForm, TaskForm
from django import forms


class ReleaseList(LoginRequiredMixin,ListView):
    model = Portfolio
    template_name = 'scrum/portfolio.html'
    context_object_name = 'portfoliolist'
    paginate_by = 20
    # model
    # get_object
    #queryset
    #def get_queryset(self):
    #    """Return the last five published questions."""
    #    #return Userstory.objects.order_by(LoginRequiredMixin,'-userstoryid')[:30]
    #    #return Userstory.objects.order_by('rank')
     #   return Portfolio.objects.all().order_by('rank')

class ReleaseDetails(LoginRequiredMixin,DetailView):
    model = PortfolioReleases
    template_name = 'scrum/releaseDetails.html'
    context_object_name = 'release'

    def get_context_data(self, *args, **kwargs):
        context = super(ReleaseDetails, self).get_context_data(*args, **kwargs)
        context['release_status'] = ReleaseStatus.objects.all()
        return context


class ReleaseCreate(LoginRequiredMixin,CreateView):
    model = PortfolioReleases

    form_class = ReleaseForm
    #success_url = reverse('scrum:portfolio-detail')
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.createby = self.request.user.username
            form.instance.portfolioid = Portfolio.objects.get(pk=self.kwargs['portfolio_id'])
            return super(ReleaseCreate, self).form_valid(form)

class ReleaseUpdate(LoginRequiredMixin,UpdateView):
    model = PortfolioReleases
    #fields =  ['releaseid','planstartdate','actualstartdate','teamid','releasestatusid','planenddate','actualenddate','details' ]
    form_class = ReleaseForm
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.updateby =  self.request.user.username
            #form.instance.portfolioid = Portfolio.objects.get(pk=self.kwargs['portfolio_id'])
            return super(ReleaseUpdate, self).form_valid(form)

class ReleaseDelete(LoginRequiredMixin,DeleteView):
    model = PortfolioReleases
    success_url = reverse_lazy('scrum:PortfolioReleasesList')
######################################
#Userstory, userstory

class UserstoryDetails(LoginRequiredMixin, DetailView):
    model = Userstory
    template_name = 'scrum/userstoryDetails.html'
    context_object_name = 'userstory'

    #def get_context_data(self, *args, **kwargs):
    #    context = super(ReleaseDetails, self).get_context_data(*args, **kwargs)
    #    context['release_status'] = ReleaseStatus.objects.all()
    #    return context

class UserstoryCreate(LoginRequiredMixin,CreateView):
    model = Userstory

    form_class =UserstoryForm
    #success_url = reverse_lazy('scrum:release-detail',Userstory.releaseid_id)
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.createby = self.request.user.username
            form.instance.releaseid = PortfolioReleases.objects.get(pk=self.kwargs['release_id'])
            return super(UserstoryCreate, self).form_valid(form)

class UserstoryUpdate(LoginRequiredMixin,UpdateView):
    model = Userstory
    form_class = UserstoryForm
    def form_valid(self, form):
        #form.instance.portfolioId
        form.instance.updateby = self.request.user.username
        return super(UserstoryUpdate, self).form_valid(form)

class UserstoryDelete(LoginRequiredMixin,DeleteView):
    model = Userstory
    success_url = reverse_lazy('scrum:PortfolioReleasesList')
##############################################33
class UserstoryCreate(LoginRequiredMixin,CreateView):
    model = Userstory

    form_class =UserstoryForm
    #success_url = reverse_lazy('scrum:release-detail',Userstory.releaseid_id)
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.createby = self.request.user.username
            form.instance.releaseid = PortfolioReleases.objects.get(pk=self.kwargs['release_id'])
            return super(UserstoryCreate, self).form_valid(form)

class UserstoryUpdate(LoginRequiredMixin,UpdateView):
    model = Userstory
    form_class = UserstoryForm
    def form_valid(self, form):
        #form.instance.portfolioId
        form.instance.updateby = self.request.user.username
        return super(UserstoryUpdate, self).form_valid(form)

class UserstoryDelete(LoginRequiredMixin,DeleteView):
    model = Userstory
    success_url = reverse_lazy('scrum:PortfolioReleasesList')
#######################
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class =TaskForm
    #success_url = reverse_lazy('scrum:userstory-detail',task.userstory_id)
    def form_valid(self, form):
        #form.instance.portfolioId
        #form.instance.createby = self.request.user.username
        form.instance.userstoryid = Userstory.objects.get(pk=self.kwargs['userstory_id'])
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    def form_valid(self, form):
        #form.instance.portfolioId
        #form.instance.userstoryid = Userstory.objects.get(pk=self.kwargs['userstory_id'])
        return super(TaskUpdate, self).form_valid(form)

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('scrum:userstory-detail',Task.userstoryid_id)
##########################################33

#Sprint, sprint

class SprintDetails(LoginRequiredMixin, DetailView):
    model = Sprint
    template_name = 'scrum/sprintDetails.html'
    context_object_name = 'sprint'

    def get_context_data(self, *args, **kwargs):
        context = super(SprintDetails, self).get_context_data(*args, **kwargs)
        #context['sprint_status'] = SprintStatus.objects.all()
        return context


class SprintCreate(LoginRequiredMixin, CreateView):
    model = Sprint
    form_class =SprintForm
    #success_url = reverse('scrum:portfolio-detail')
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.createby = self.request.user
            form.instance.releaseid = PortfolioReleases.objects.get(pk=self.kwargs['release_id'])
            return super(SprintCreate, self).form_valid(form)

class SprintUpdate(LoginRequiredMixin,UpdateView):
    model = Sprint
    form_class = SprintForm
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.updateby = self.request.user
            return super(SprintUpdate, self).form_valid(form)

class SprintDelete(LoginRequiredMixin,DeleteView):
    model = Sprint
    success_url = reverse_lazy('scrum:PortfolioReleasesList')
'''
class Sprint_userstorySelect(LoginRequiredMixin,ListView):
    model = Userstory
    template_name = 'scrum/userstory_multiselect.html'
    context_object_name = 'userstory'
    paginate_by = 20
    # model
    # get_object
    # queryset
    #def get_queryset(self):
    #    """Return the last five published questions."""
     #   return Userstory.objects.get(pk=1)
'''