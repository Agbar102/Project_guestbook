from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

from .models import Message
from .forms import MessageForm

#Отображаются только одобренные (is_visible=True) записи
#Страница со списком сообщений
def guestbook_list(request):
    messages_list = Message.objects.filter(is_visible=True)
    return render(request, 'guestbook/list.html', {'messages': messages_list})

#Уведомление о публикации после отправки
def guestbook_add(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES) # чтоб можно было еще аватар добавить
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше сообщение отправлено и будет опубликовано после одобрения.")
        return redirect('guestbook_list')
    else:
        form = MessageForm()
    return render(request, 'guestbook/add.html', {'form': form})


def index(request):
    form = MessageForm()
    return render(request, 'pages/index.html', {'form': form})


def home_view(request):
    latest_posts = Message.objects.filter(is_visible=True).order_by('-created_at')[:3]
    return render(request, 'index.html', {'latest_posts': latest_posts})



def guestbook_list(request):
    query = request.GET.get('q')
    if query:
        messages_list = Message.objects.filter(
            Q(is_visible=True) & (Q(name__icontains=query) | Q(text__icontains=query))
        )
    else:
        messages_list = Message.objects.filter(is_visible=True)
    return render(request, 'guestbook/list.html', {'messages': messages_list})
