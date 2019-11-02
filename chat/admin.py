from django.contrib import admin
from . import models

# Register your models here.

class ChatAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('user','message','status',)
    list_filter = ('status', 'date_add', )
    search_fields = ('message',)
    
admin.site.register(models.Chat, ChatAdmin)