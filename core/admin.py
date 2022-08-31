from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([User])

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request) -> bool:
        return False
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
@admin.register(Statistics)
class StatiticsAdmin(admin.ModelAdmin):
    list_display= ['twitter', 'discord']
    # list_editable = ['twitter', 'discord']
    list_display_links = ['twitter', 'discord']