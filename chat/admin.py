from .models import Chat, Message
from django.contrib import admin

"""
    Django admin configuration for the Message model with specific fields for display, editing, and searching.
"""

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'text', 'created_at', 'author', 'receiver') 
    list_display = ('text', 'created_at', 'author', 'receiver') 
    search_fields = ('text',) 


admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
