from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Message
from .forms import MessageForm


def guestbook_list(request):
    query = request.GET.get('q')
    messages_list = Message.objects.filter(is_visible=True)
    if query:
        messages_list = messages_list.filter(Q(name__icontains=query) | Q(text__icontains=query))
    return render(request, 'guestbook/list.html', {'messages': messages_list})


def main_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше сообщение отправлено и будет опубликовано после одобрения.")
        return redirect('guestbook_list')
    else:
        form = MessageForm()

    latest_posts = Message.objects.filter(is_visible=True).order_by('-created_at')[:3]
    context = {
        'form': form,
        'latest_posts': latest_posts
    }
    return render(request, 'pages/index.html', context)




