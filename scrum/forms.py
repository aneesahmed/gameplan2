from django import forms
import datetime
from django.contrib.admin import widgets
from .models import Portfolio , PortfolioReleases, PortfolioStatus,Userstory


class UserstoryForm(forms.ModelForm):

    class Meta:
        model = Userstory
        fields = "__all__"
        #labels =
        widgets = {'details': forms.Textarea(attrs={'cols': 80})}

class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ['title','portfoliotypeid','owner','details','rank','portfoliostatusid']
        labels = {'title': 'Title','portfoliotypeid':'PortFolio Type','portfoliostatusid':'Status'}
        widgets = {'details': forms.Textarea(attrs={'cols': 80})}

class ReleaseForm(forms.ModelForm):

    class Meta:
        model = PortfolioReleases
        #fields = "__all__"

        fields = ['portfolioid', 'details','planstartdate','actualstartdate','planenddate','actualenddate','teamid']
        widgets = {'actualstartdate': forms.DateInput(attrs={'class':'datepicker'}),
                   'details': forms.Textarea(attrs={'cols': 80})}

        #labels = {'title': 'Title','portfoliotypeid':'PortFolio Type','portfoliostatusid':'Status'}