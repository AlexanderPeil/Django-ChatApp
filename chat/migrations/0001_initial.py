# Generated by Django 4.2.4 on 2023-08-22 09:56
# Eine Djanog_Migration 

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True # Die erste Migration für diese App

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL), # Diese Migration ist abhängig von der Migration "AUTH_USER_MODEL"
    ]
    # Operationen, die diese Migration ausführen soll. 
    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('created_at', models.DateField(default=datetime.datetime.today)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_message_set', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_message_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]


#Zusammengefasst: Dieser Code repräsentiert eine Migration, die ein neues Message-Modell in Ihrer Datenbank erstellt. 
# Dieses Modell enthält Felder für den Nachrichtentext, ein Erstellungsdatum und Fremdschlüsselfelder für den Autor und den Empfänger der Nachricht. 
# Das Modell ist auch abhängig von einem anderen Modell, das in den Einstellungen als AUTH_USER_MODEL definiert ist.