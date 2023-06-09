from django.contrib import admin
from .models import *


admin.site.register(CustomUser)
admin.site.register(CompanyUser)
admin.site.register(CandidateUser)
admin.site.register(JobAdd)
admin.site.register(Application)