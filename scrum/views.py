from django.shortcuts import render
from django.http import HttpResponse
from  scrum.models import PortfolioStatus, Portfolio
from django.template import loader
from django.http import Http404
#def index(request):
#    return HttpResponse("scrum dashboard.")
def index(request):
    #status = Portfoliostatus.objects.order_by('ordering')[:1]
    status = PortfolioStatus.objects.filter(portfoliostatusid=2)
    statusFilter = status.values_list("portfoliostatusid", flat=True) 
    pflist = Portfolio.objects.order_by('rank')[:5]
    template = loader.get_template('scrum/index.html')
    context = {
        'pflist': pflist,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'scrum/index.html', context)
    #output = ', '.join([st.title for st in status])
    #return HttpResponse(output + "ting" + str(statusFilter[0]))

def portfolioAdd(request):
    #return HttpResponse(output)
    return render(request, 'scrum/newPortfolio.html')    
def portfolio(request):
    id = 1
    portfolio = Portfolio
    try:
        portfolio = Portfolio.objects.get(pk=id)
    except portfolio.DoesNotExist:
        raise Http404("portfolio does not exist")
    return render(request, 'scrum/portfolio.html', {'portfolio': portfolio})