from django.shortcuts import render
from main.models import Message

import user_auth.py


def front(request):
    return render(request, 'index.html', {})


def all_messages(request):
    messages = Message.objects.all().order_by('-date_posted')

    return render(request, 'all_messages.html', {'messages': messages})
