import logging

from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm

log = logging.getLogger(__name__)


def login_view(request):
    print('Пользователь', request.user.is_authenticated)
    next = request.GET.get('next')
    title = "Авторизация пользователя"
    button = "Войти"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "form": form,
        "title": title,
        "button": button
    }
    return render(request, "accounts/form.html", context)


def register_view(request):
    print(request.user.is_authenticated)
    next = request.GET.get('next')
    title = "Регистрация пользователя"
    button = "Принять"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": title,
        "button": button
    }
    return render(request, "accounts/form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")

