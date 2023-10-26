from django.shortcuts import render, redirect
from .models import Chat, Message
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.http import JsonResponse
from django.core import serializers


@login_required(login_url='/login/')
def index(request):
    """
    Handles chat messages by processing new messages for POST requests and displaying existing messages for GET requests.
    """
    if request.method == 'POST': 
        myChat = Chat.objects.get(id=1) 
        new_Message = Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
        serialized_obj = serializers.serialize('json', [ new_Message, ]) 
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages' : chatMessages}) 


def login_view(request):
    """
    Handles the login functionality.

    """
    redirect = request.GET.get('next') or '/chat'
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))        
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
             return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})


def signup_view(request):
    """
    Handles the user registration functionality.

    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})
    

def logout_view(request):
    """
    Handles the user logout functionality.

    """
    logout(request)
    return redirect('login')

