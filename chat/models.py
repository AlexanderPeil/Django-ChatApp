# models.py:
# 1.) Definiert die Datenmodelle der App, die die Struktur der Datenbanktabellen repräsentieren.
# 2.) Jede Klasse in models.py repräsentiert in der Regel eine Tabelle in der Datenbank.


# 
from datetime import datetime # Wird importiert, um auf die aktuelle Zeit zuzugreifen, die als Standardwert für einige der Modelle verwendet wird.
from django.db import models # Wird von Django bereitgestellt und enthält Klassen und Funktionen, um Datenbankmodelle zu definieren.
from django.conf import settings #  Ein Modul in Django, das Zugriff auf die Projekt-Konfigurationseinstellungen ermöglicht, insbesondere AUTH_USER_MODEL, das auf das benutzerdefinierte Benutzermodell verweist, falls vorhanden.


# Das Chat-Modell hat ein einziges Feld:
# created_at: Ein Datumfeld, das automatisch auf das aktuelle Datum eingestellt wird, wenn ein neuer Chat-Eintrag erstellt wird.
class Chat(models.Model):
        created_at = models.DateField(default=datetime.today)


# Das Message-Modell repräsentiert eine Nachricht in einem Chat und enthält mehrere Felder:
class Message(models.Model):
    text = models.CharField(max_length=500) #  Ein Zeichenfeld (CharField) mit einer maximalen Länge von 500 Zeichen, das den eigentlichen Nachrichtentext speichert.
    created_at = models.DateField(default=datetime.today) #  Ähnlich wie im Chat-Modell ist dies ein Datumfeld, das automatisch auf das aktuelle Datum eingestellt wird, wenn eine neue Nachricht erstellt wird.
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True) #  Ein Fremdschlüsselfeld (ForeignKey), das eine Beziehung zwischen einer Nachricht und einem bestimmten Chat herstellt. Das on_delete=models.CASCADE bedeutet, dass, wenn ein Chat gelöscht wird, alle damit verbundenen Nachrichten auch gelöscht werden. Der Parameter related_name gibt einen Namen für die Rückbeziehung vom Chat-Modell zur Message-Entität an.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set') 
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')
    # author und receiver: Beide sind Fremdschlüsselfelder, die auf das Benutzermodell zeigen (standardmäßig das eingebaute User-Modell von Django oder ein benutzerdefiniertes Modell, falls festgelegt). Sie repräsentieren den Absender (Autor) und den Empfänger einer Nachricht. Auch hier führt das Löschen eines Benutzers (durch on_delete=models.CASCADE) dazu, dass alle Nachrichten, die von diesem Benutzer gesendet oder an ihn gerichtet wurden, gelöscht werden. Die related_name-Parameter ermöglichen den Zugriff auf alle Nachrichten, die von einem bestimmten Benutzer gesendet bzw. an ihn gesendet wurden.

    # Zusammenfassend stellt dieser Code Datenstrukturen für ein einfaches Chat-System bereit, in dem Benutzer Nachrichten in Chats senden und empfangen können.