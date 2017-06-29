from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import Http404
from scrum.forms import UserstoryForm
from django.core.urlresolvers import reverse
from  scrum.models import PortfolioStatus, Portfolio, PortfolioReleases, Userstory
from django.views.generic import ListView, DetailView
from scrum.submodels.portfolioReleasemodel import Userstory

# unassigned
# release wise filter
# a user story must belogn to a release of a portfolio

@login_required
class userstoryList(ListView):
    template_name = 'scrum/userstory.html'
    context_object_name = 'userstory'

    def get_queryset(self):
        """Return the last five published questions."""
        #return Userstory.objects.order_by('-userstoryid')[:30]
        return Userstory.objects.order_by('-userstoryid')


@login_required
def new_userstory(request):
    if request.method != 'POST':
        form = UserstoryForm()
        context = {'form': form}
        return render(request, 'scrum/userstory_form.html', context)


def userstoryUpdate(request, id=-1):
    if request.method != 'POST':
        userstory = Userstory.objects.get(userstoryid=id)
        form = UserstoryForm(instance=userstory)
        context = {'userStory': userstory, 'form': form}
        return render(request, 'scrum/userstory_form.html', context)
    else:
        if id== -1:
            form = UserstoryForm(data=request.POST)
        else:
            # change in the form
            portfolio = UserStory.objects.get(portfolioid=id)
            form = UserstoryForm(instance=portfolio, data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse(('scrum:portfolio')))
        else:
            return HttpResponse("invalid form.")
