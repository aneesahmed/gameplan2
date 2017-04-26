from django.contrib import admin

from .models import Portfoliostatus
from .models import Portfoliotype
from .models import Resourcetype
from .models import Resource
from .models import Team
from .models import TeamResource
from .models import Portfolio

admin.site.register(Portfoliostatus)
admin.site.register(Portfoliotype)
admin.site.register(Resourcetype)
admin.site.register(Resource)
admin.site.register(Team)
admin.site.register(TeamResource)
admin.site.register(Portfolio)