from django.contrib import admin

# Register your models here.

from ACS.apps.contracts.models import *

admin.site.register(Contracts)
admin.site.register(Organization)
admin.site.register(OrganizationInfo)

