from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from  scrum.models import PortfolioStatus, Portfolio, PortfolioReleases, Userstory
from django.template import loader
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView


class PortfolioList(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = 'scrum/portfolio_list.html'
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
    def get_context_data(self, *args, **kwargs):
        context = super(PortfolioList, self).get_context_data(*args, **kwargs)
        context['portfolio_status'] = PortfolioStatus.objects.all()
        return context

class PortfolioListbyStatus(LoginRequiredMixin, ListView):
    model = Portfolio
    tempelate_name = 'scrum/portfolio.html'
    context_object_name = 'portfoliolist'
    paginate_by = 20

    def get_queryset(self):
        status = int(self.kwargs['status_id'])
        if (status>0):
            return Portfolio.objects.all().filter(portfoliostatusid=status)
        else:
            return Portfolio.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(PortfolioListbyStatus, self).get_context_data(*args, **kwargs)
        context['portfolio_status'] = PortfolioStatus.objects.all()
        return context

'''
class Dashboard(LoginRequiredMixin, TemplateView):
        template_name = "scrum/dashboard.html"

        def get_context_data(self, **kwargs):
            context = super(Dashboard, self).get_context_data(**kwargs)
            context['latest_portfolios'] = Portfolio.objects.all()[:5]
            context['portfolio_status'] = PortfolioStatus.objects.all()
            return context
'''
class PortfolioDetails(LoginRequiredMixin,DetailView):
    model = Portfolio
    template_name = 'scrum/portfolioDetails.html'
    context_object_name = 'portfolio'

    def get_context_data(self, *args, **kwargs):
        context = super(PortfolioDetails, self).get_context_data(*args, **kwargs)
        context['portfolio_status'] = PortfolioStatus.objects.all()
        return context

class PortfolioCreate(LoginRequiredMixin,CreateView):
    model = Portfolio
    fields =  ['title','portfoliotypeid','owner','details','rank','portfoliostatusid' ]

    def form_valid(self, form):
            form.instance.createby = self.request.user.username
            return super(PortfolioCreate, self).form_valid(form)

class PortfolioUpdate(LoginRequiredMixin,UpdateView):
    model = Portfolio
    fields =  ['title','portfoliotypeid','owner','details','rank','portfoliostatusid' ]
    def form_valid(self, form):
            #form.instance.portfolioId
            form.instance.updateby =  self.request.user.username
            #form.instance.portfolioid = Portfolio.objects.get(pk=self.kwargs['portfolio_id'])
            return super(PortfolioUpdate, self).form_valid(form)

class PortfolioDelete(LoginRequiredMixin,DeleteView):
    model = Portfolio
    success_url = reverse_lazy('scrum:portfolioList')

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
        return render(request, 'scrum/portfolioreleases_form.html', context)


'''