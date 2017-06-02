from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from  scrum.models import PortfolioStatus, Portfolio, PortfolioReleases, Userstory
from django.template import loader
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView


class PortfolioList(ListView):
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
    template_name = 'scrum/portfolioDetails.html'
    context_object_name = 'portfolio'

    def get_context_data(self, *args, **kwargs):
        context = super(ReleaseDetails, self).get_context_data(*args, **kwargs)
        context['portfolio_status'] = ReleaseDetails.objects.all()
        return context

class ReleaseCreate(CreateView):
    model = PortfolioReleases
    fields =  ['releaseid','planstartdate','actualstartdate','teamid','planenddate','actualenddate','details' ]
    #hide or send this field  to choose current portfolio automatically
    #portfolioid
    def form_valid(self, form):
            form.instance.createby = self.request.user
            return super(ReleaseCreate, self).form_valid(form)

class ReleaseUpdate(UpdateView):
    model = PortfolioReleases
    fields =  ['releaseid','planstartdate','actualstartdate','teamid','planenddate','actualenddate','details' ]

class ReleaseDelete(DeleteView):
    model = PortfolioReleases
    success_url = reverse_lazy('scrum:PortfolioReleasesList')

######################################
