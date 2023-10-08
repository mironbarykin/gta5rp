from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Вы уже вошли в аккаунт.")
        return redirect('documents')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('documents')
            else:
                messages.error(request, 'Неправильное имя пользователя или пароль.')

        return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    return redirect('authentication.login')


def appeal_view(request):
    messages.error(request, 'В разработке.')
    logout(request)
    return redirect('authentication.login')
