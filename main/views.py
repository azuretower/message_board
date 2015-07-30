from django.shortcuts import render
from main.models import Message
from django.contrib.auth.decorators import login_required, user_passes_test
from main.forms import MessageForm
from django.http import HttpResponse

import user_auth
from user_auth import is_super


@login_required
def front(request):

    # posts = Post.objects.all().order_by('-date_posted')

    context = {}

    if request.method == 'POST':

        # id = request.POST.get('id')

        # if id:

        #     message = Message.objects.get(id=id)
        #     form = PostForm(request.POST, request.FILES, instance=post)

        # else:

        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save()
            context['result'] = 'Your post has been saved'
        else:
            context['result'] = form.errors

    return render(request, 'index.html', context)


@login_required
# @user_passes_test(is_super)
def all_messages(request):
    messages = Message.objects.all().order_by('-date_posted')

    return render(request, 'all_messages.html', {'messages': messages})


def edit_message(request, id):

    if request.method == 'DELETE':

        if request.user.is_superuser:

            Message.objects.get(id=id).delete()

            return HttpResponse(status=204)
        else:
            return HttpResponse(status=401)

    elif request.method == 'GET':
        message = Message.objects.get(id=id)

        return render(request, 'message.html', {'message': message})
