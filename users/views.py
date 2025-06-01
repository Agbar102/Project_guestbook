from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from users.serializers import RegisterUserSerializer




User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        data = request.POST.dict()
        serializer = RegisterUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('login')
    else:
        serializer = RegisterUserSerializer()
    return render(request, 'registration/register.html', {'form': serializer})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm


def custom_logout_view(request):
    logout(request)
    return redirect('index')
