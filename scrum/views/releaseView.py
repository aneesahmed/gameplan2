from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from  scrum.models import PortfolioStatus, Portfolio, PortfolioReleases, Userstory,ReleaseStatus, Sprint
from django.template import loader
from django.urls import reverse_lazy,reverse
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from scrum.forms import ReleaseForm, UserstoryForm, SprintForm
from django import forms


class ReleaseList(ListView):
    model = Portfolio
    template_name = 'scrum/portfolio.html'
    context_object_name = 'portfoliolist'
    paginate_by = 20
    # model
    # get_object
    #queryset
    #def get_queryset(self):
    #    """Return the last five published questions."""
    #    #return Userstory.objects.order_by('-userstoryid')[:30]
    #    #return Userstory.objects.order_by('rank')
     #   return Portfolio.objects.all().order_by('rank')

class ReleaseDetails(DetailView):
    model = PortfolioReleases
    template_name = 'scrum/releaseDetails.html'
    context_object_name = 'release'

    def get_context_data(self, *args, **kwargs):
        context = super(ReleaseDetails, self).get_context_data(*args, **kwargs)
        context['release_status'] = ReleaseStatus.objects.all()
        return context


class ReleaseCreate(CreateView):
    model = PortfolioReleases

    form_class = ReleaseForm
    #success_url = reverse('scrum:portfolio-detail')
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.createby = self.request.user
            form.instance.portfolioid = Portfolio.objects.get(pk=self.kwargs['portfolio_id'])
            return super(ReleaseCreate, self).form_valid(form)

class ReleaseUpdate(UpdateView):
    model = PortfolioReleases
    #fields =  ['releaseid','planstartdate','actualstartdate','teamid','releasestatusid','planenddate','actualenddate','details' ]
    form_class = ReleaseForm
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.updateby =  self.request.user._wrapped if hasattr(self.request.user,'_wrapped') else self.request.user
            #form.instance.portfolioid = Portfolio.objects.get(pk=self.kwargs['portfolio_id'])
            return super(ReleaseUpdate, self).form_valid(form)

class ReleaseDelete(DeleteView):
    model = PortfolioReleases
    success_url = reverse_lazy('scrum:PortfolioReleasesList')
######################################
#Userstory, userstory

class UserstoryCreate(CreateView):
    model = Userstory

    form_class =UserstoryForm
    #success_url = reverse('scrum:portfolio-detail')
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.createby = self.request.user
            form.instance.releaseid = PortfolioReleases.objects.get(pk=self.kwargs['release_id'])
            return super(UserstoryCreate, self).form_valid(form)

class UserstoryUpdate(UpdateView):
    model = Userstory
    form_class = UserstoryForm
    def form_valid(self, form):
        #form.instance.portfolioId
        form.instance.updateby = self.request.user._wrapped if hasattr(self.request.user,'_wrapped') else self.request.user
        return super(UserstoryUpdate, self).form_valid(form)

class UserstoryDelete(DeleteView):
    model = Userstory
    success_url = reverse_lazy('scrum:PortfolioReleasesList')

#Sprint, sprint
class SprintCreate(CreateView):
    model = Sprint
    form_class =SprintForm
    #success_url = reverse('scrum:portfolio-detail')
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.createby = self.request.user
            form.instance.releaseid = PortfolioReleases.objects.get(pk=self.kwargs['release_id'])
            return super(UserstoryCreate, self).form_valid(form)

class SprintUpdate(UpdateView):
    model = Sprint
    form_class = SprintForm
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.updateby = self.request.user
            return super(UserstoryUpdate, self).form_valid(form)

class SprintDelete(DeleteView):
    model = Sprint
    success_url = reverse_lazy('scrum:PortfolioReleasesList')