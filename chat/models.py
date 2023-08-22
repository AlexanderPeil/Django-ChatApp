from datetime import datetime
from django.db import models
from django.conf import settings

class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=datetime.today)
    # chat = Chat Klasse verknüpfen
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')