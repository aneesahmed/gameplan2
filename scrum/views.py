from django.shortcuts import render
from django.http import HttpResponse
from  scrum.models import Portfoliostatus, Portfolio
from django.template import loader

#def index(request):
#    return HttpResponse("scrum dashboard.")
def index(request):
    #status = Portfoliostatus.objects.order_by('ordering')[:1]
    status = Portfoliostatus.objects.filter(portfoliostatusid=2)
    statusFilter = status.values_list("portfoliostatusid", flat=True) 
    pflist = Portfolio.objects.order_by('rank')[:5]
    template = loader.get_template('scrum/index.html')
    context = {
        'pflist': pflist,
    }
    return HttpResponse(template.render(context, request))

    #output = ', '.join([st.title for st in status])
    #return HttpResponse(output + "ting" + str(statusFilter[0]))

def portfolio(request, statusId):
    return HttpResponse("You're looking at status id %s." % statusId)