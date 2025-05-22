from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.template.context_processors import request
from users.serializers import RegisterUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


User = get_user_model()


class RegisterUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            user = User(email=email)
            user.set_password(password)
            user.save()
        return Response({"message": "ПОЛЬЗОВАТЕЛЬ СОЗДАН"})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm


def custom_logout_view(request):
    logout(request)
    return redirect('index')
