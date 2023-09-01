# Admin.py:
# 1.) Definiert die Darstellung Ihrer Modelle im Django Admin-Interface.
# 2.) Ermöglicht die Anpassung des Verhaltens, der Darstellung und anderer Aspekte des Admin-Interfaces für jedes Modell.



# Hier werden die Chat und Message Modelle aus der models.py Datei des aktuellen Django-Apps-Verzeichnisses importiert. 
# Zudem wird das admin Modul von django.contrib importiert, welches benötigt wird, um das Admin-Interface anzupassen.
from .models import Chat, Message
from django.contrib import admin

# Die MessageAdmin Klasse erbt von admin.ModelAdmin und ermöglicht die Anpassung
# des Verhaltens und der Darstellung des Message-Modells im Admin-Interface.
class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'text', 'created_at', 'author', 'receiver') #Bestimmt die Reihenfolge und Auswahl der Felder, die im Formular angezeigt werden, wenn man eine Nachricht bearbeitet oder hinzufügt.
    list_display = ('text', 'created_at', 'author', 'receiver') # Legt fest, welche Felder in der Liste aller Nachrichten angezeigt werden.
    search_fields = ('text',) # Bestimmt, welche Felder durchsuchbar sind. Hier kann man im Admin-Interface nach Nachrichtentexten suchen.

# Register your models here.
# Mit diesen Zeilen werden die Modelle Message und Chat für das Django Admin-Interface registriert.
admin.site.register(Message, MessageAdmin)# Beim Registrieren des Message-Modells wird zudem angegeben, dass das Admin-Interface dieses Modells durch die MessageAdmin-Klasse angepasst werden soll.
admin.site.register(Chat)

# Zusammengefasst: Der gegebene Code ermöglicht es, das Chat und Message Modell über das Django Admin-Interface zu verwalten. 
# Für das Message-Modell gibt es zudem einige spezifische Anpassungen, wie z.B. die Suchfunktion und die angezeigten Felder.