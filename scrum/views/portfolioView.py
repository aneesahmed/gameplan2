from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from  scrum.models import PortfolioStatus, Portfolio, PortfolioReleases, Userstory
from django.template import loader
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class PortfolioList(ListView):
    model = Portfolio
    template_name = 'scrum/portfolio.html'
    context_object_name = 'portfoliolist'
    paginate_by = 20

    #def get_queryset(self):
    #    """Return the last five published questions."""
    #    #return Userstory.objects.order_by('-userstoryid')[:30]
    #    #return Userstory.objects.order_by('rank')
     #   return Portfolio.objects.all().order_by('rank')



class PortfolioDetails(DetailView):
    model = Portfolio
    template_name = 'scrum/portfolioDetails.html'
    context_object_name = 'portfolio'

class PortfolioCreate(CreateView):
    model = Portfolio
    #fields =  []

class PortfolioUpdate(UpdateView):
    model = Portfolio


class PortfolioDelete(DeleteView):
    model = Portfolio
######################################
'''
def index(request):
    return render(request, "scrum/index.html")

@login_required
def portfolioList(request):
    # status = Portfoliostatus.objects.order_by('ordering')[:1]
    #status = PortfolioStatus.objects.filter(portfoliostatusid=2)
    #statusFilter = status.values_list("portfoliostatusid", flat=True)
    pflist = Portfolio.objects.order_by('rank')
    #template = loader.get_template('scrum/index.html')
    context = {
        'pflist': pflist,
    }
    return render(request, 'scrum/portfolio.html', context)

@login_required
def portfolioDetails(request, id):
    #Show a single  record with its sub entries
    portfolio = Portfolio.objects.get(portfolioid=id)
    #if topic.owner != request.user:
    #    raise Http404
    releases = portfolio.portfolioreleases_set.order_by('-releaseid')

    context = {'portfolio': portfolio, 'releases': releases}
    return render(request, 'scrum/portfolioDetails.html', context)



@login_required
def new_sprint(request):
    if request.method != 'POST':
        form = SprintForm()
        context = {'form': form}
        return render(request, 'scrum/sprintForm.html', context)


def sprintUpdate(request, id=-1):
    if request.method != 'POST':
        sprint = Sprint.objects.get(userstoryid=id)
        form = SprintForm(instance=userstory)
        context = {'sprint': sprint, 'form': form}
        return render(request, 'scrum/sprintyForm.html', context)
    else:
        if id== -1:
            form = SprintForm(data=request.POST)
        else:
            # change in the form
            sprint = Sprint.objects.get(portfolioid=id)
            form = SprintForm(instance=portfolio, data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse(('scrum:portfolio')))
        else:
            return HttpResponse("invalid form.")


################################33333


@login_required
def new_release(request):
    if request.method == "POST":
        form = ReleaseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # release = form.save(commit=True)
            # portfolio.author = request.user
            # portfolio.published_date = timezone.now()
            # release.save()
            # we will send it back to portfolio update form
            return HttpResponseRedirect(reverse(('scrum:portfolio')))
        else:
            return HttpResponse("invalid form.")

    else:
        form = ReleaseForm()
        context = {'form': form}
        return render(request, 'scrum/releaseForm.html', context)


'''