from datetime import datetime 
from django.db import models 
from django.conf import settings 


"""Represents a chat instance with a creation date."""
class Chat(models.Model):
        created_at = models.DateField(default=datetime.today)


"""
        Represents a chat message with text, creation date, associated chat, author, and receiver.
"""
class Message(models.Model):
    text = models.CharField(max_length=500) 
    created_at = models.DateField(default=datetime.today) 
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True) 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set') 
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')
   