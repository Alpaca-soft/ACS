from django.contrib import admin

from ACS.apps.accounts.contacts.models import Contact


admin.site.register(Contact)
"""
class UserProfileAdmin(admin.ModelAdmin):

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset

    user_info.short_description = 'Info'

    admin.site.register(UserProfile, UserProfileAdmin)
"""