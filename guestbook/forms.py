from django import forms
from .models import Message

#Создание формы для отправки сообщений
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'text', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ваш email'}),
            'text': forms.Textarea(attrs={'placeholder': 'Ваше сообщение'}),

        }