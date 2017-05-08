from django.shortcuts import render,HttpResponse
from  scrum.models import PortfolioStatus, Portfolio
from django.template import loader
from django.http import Http404
from .forms import PortfolioForm
from django.core.urlresolvers import reverse



def newPortfolio(request):
    #return HttpResponse("scrum dashboard.")
    #Add  new
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PortfolioForm()
    else:
    # POST data submitted; process data.
    form = PortfolioForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("scrum:portfolioDashboard"))

def portfolioDashboard(request):
    #status = Portfoliostatus.objects.order_by('ordering')[:1]
    status = PortfolioStatus.objects.filter(portfoliostatusid=2)
    statusFilter = status.values_list("portfoliostatusid", flat=True) 
    pflist = Portfolio.objects.order_by('rank')[:5]
    template = loader.get_template('scrum/index.html')
    context = {
        'pflist': pflist,
    }
    return render(request, 'scrum/portfolioDashboard.html', context)


def portfolio(request, id):
    context = {
        'id': id,
    }
    return render(request, 'scrum/portfolio.html', context)