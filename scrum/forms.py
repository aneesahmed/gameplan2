from django import forms
import datetime
from django.contrib.admin import widgets
from .models import Portfolio , PortfolioReleases, PortfolioStatus,Userstory, Sprint
from django.contrib.admin.widgets import AdminDateWidget


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
        widgets = {'details': forms.Textarea(attrs={'cols': 40,'rows':3})}

class ReleaseForm(forms.ModelForm):

    class Meta:
        model = PortfolioReleases
        #fields = "__all__"

        fields = [ 'details','releasestatusid','planstartdate','actualstartdate','planenddate','actualenddate','teamid']
        widgets = {'details': forms.Textarea(attrs={'cols': 30,'rows':3}),
                   'planstartdate': forms.SelectDateWidget,
                   'actualstartdate': forms.SelectDateWidget,
                   'planenddate': forms.SelectDateWidget,
                   'actualenddate': forms.SelectDateWidget
                   }

        labels = {'title': 'Title','portfoliotypeid':'PortFolio Type','portfoliostatusid':'Status'}

class UserstoryForm(forms.ModelForm):

    class Meta:
        model = Userstory
        #fields = "__all__"

        fields = [ 'details', 'sprintid','createby','createdate','updateby','updatedate']
        widgets = {'details': forms.Textarea(attrs={'cols': 20,'rows':3}),
                   'createby':forms.TextInput(attrs={'readonly':'readonly'}),
                   'updateby': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'createdate': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'updatedate': forms.TextInput(attrs={'readonly': 'readonly'}),
                   }


class SprintForm(forms.ModelForm):

    class Meta:
        model = Sprint
        #fields = "__all__"

        fields = [ 'sprintid','details','releaseId','enddate','startdate', 'createby','createdate','updateby','updatedate']
        widgets = {'details': forms.Textarea(attrs={'cols': 20,'rows':3}),
                   'startdate': forms.SelectDateWidget,
                   'enddate': forms.SelectDateWidget,
                   'sprintid': forms.TextInput(attrs={'readonly':'readonly'}),
                   'createby':forms.TextInput(attrs={'readonly':'readonly'}),
                   'updateby': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'createdate': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'updatedate': forms.TextInput(attrs={'readonly': 'readonly'}),
                   }