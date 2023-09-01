# views-py:
# 1.) Definiert die Ansichten (Logik), die bestimmen, was passiert, wenn eine bestimmte URL angefordert wird.
# 2.) Jede Funktion oder Klasse in views.py repräsentiert in der Regel eine Seite oder ein Endpoint der Webanwendung.



from django.shortcuts import render, redirect
from .models import Chat, Message
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


# Der index View ist durch den @login_required-Dekorator geschützt. Das bedeutet, dass nur eingeloggte Benutzer auf diese Ansicht zugreifen können. Wenn ein nicht eingeloggter Benutzer versucht, darauf zuzugreifen, wird er zur Anmeldeseite (/login/) weitergeleitet.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST': # Wenn die Methode der Anfrage POST ist, wird angenommen, dass der Benutzer eine neue Nachricht über das Formular gesendet hat. Die gesendete Nachricht wird dann in der Datenbank gespeichert.
        print('Received data ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1) # Unabhängig von der Anfragemethode werden alle Nachrichten, die zu einem bestimmten Chat (mit der ID 1) gehören, aus der Datenbank abgerufen.
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages' : chatMessages}) # Schließlich wird die chat/index.html-Vorlage gerendert und die abgerufenen Nachrichten an die Vorlage übergeben.


# Der login_view verarbeitet sowohl GET- als auch POST-Anfragen:
def login_view(request):
    redirect = request.GET.get('next') # Bei einem GET-Aufruf wird einfach die Login-Seite gerendert.
    # Bei einem POST-Aufruf (wenn der Benutzer das Anmeldeformular abschickt) wird versucht, den Benutzer zu authentifizieren.
    # Wenn die Authentifizierung erfolgreich ist, wird der Benutzer eingeloggt und zu einer zuvor festgelegten Weiterleitungs-URL oder einem Standardpfad weitergeleitet.
    # Wenn die Authentifizierung fehlschlägt, wird die Login-Seite erneut mit einem Fehlerhinweis gerendert.
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
             return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})
    



    # Zusammengefasst handelt es sich hierbei um einen einfachen Chat- und Login-Mechanismus.
    #  Die index-Ansicht ermöglicht es Benutzern, Nachrichten zu senden und anzuzeigen, während die login_view-Ansicht den Login-Prozess steuert.
    #  Es gibt allerdings noch einiges an Kontext, der fehlt, um das gesamte System vollständig zu verstehen – wie zum Beispiel die HTML-Vorlagen,
    #  das URL-Routing oder andere ergänzende Views.