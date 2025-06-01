from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Message
from .forms import MessageForm


def guestbook_list(request):
    query = request.GET.get('q')
    messages_list = Message.objects.filter(is_visible=True)
    if query:
        messages_list = messages_list.filter(Q(name__icontains=query) | Q(text__icontains=query) | Q(gmail__icontains=query))
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


def guestbook_edit(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if message.user != request.user:
        messages.error(request, "Вы можете редактировать только свои сообщения.")
        return redirect('guestbook_edit', pk=message.pk)

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, "Сообщение успешно обновлено.")
            return redirect('guestbook_list')
    else:
        form = MessageForm(instance=message)

    return render(request, 'guestbook/edit.html', {'form': form, 'message': message})


def guestbook_delete(request, pk):
    message = get_object_or_404(Message, pk=pk,)

    if message.user != request.user:
        messages.error(request, "Вы можете удалять только свои сообщения.")
        return redirect('guestbook_edit')

    if request.method == 'POST':
        message.delete()
        messages.success(request,  "Сообщение удалено успешно.")
        return redirect("guestbook_list")
    return render(request, "guestbook/delete_message.html", {'message': message})






