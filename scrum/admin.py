from django.contrib import admin

from .models import PortfolioStatus
from .models import PortfolioType
from .models import ResourceType
from .models import Resource
from .models import Team
from .models import TeamResource
from .models import Portfolio
from .models import PortfolioReleases
from .models import  UserStory

admin.site.register(PortfolioStatus)
admin.site.register(PortfolioType)
admin.site.register(ResourceType)
admin.site.register(Resource)
admin.site.register(Team)
admin.site.register(TeamResource)
admin.site.register(Portfolio)
admin.site.register(PortfolioReleases)
admin.site.register(UserStory)
