from django.shortcuts import render

from django.shortcuts import render, redirect
from guestbook.models import Message
from .forms import MessageForm
from django.contrib import messages

#Отображаются только одобренные (is_visible=True) записи
#Страница со списком сообщений
def guestbook_list(request):
    messages_list = Message.objects.filter(is_visible=True)
    return render(request, 'guestbook/list.html', {'messages': messages_list})

#Уведомление о публикации после отправки
def guestbook_add(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше сообщение отправлено и будет опубликовано после одобрения.")
        return redirect('guestbook_list')
    else:
        form = MessageForm()
    return render(request, 'guestbook/add.html', {'form': form})
