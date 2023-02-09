from django.shortcuts import render, redirect
from verstsite.users.forms import RegisterForm
from django.contrib.auth.hashers import make_password
from loguru import logger
from django.contrib import messages
from django.contrib.auth import login
from django.utils.html import format_html

# Create your views here.


def register(request):

    if request.method == 'POST':

        if request.POST['action'] == 'Регистрация':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data['password']
                user.password = make_password(password)
                user.save()
                login(request, user)
                message = format_html(f'Вы успешно зарегистрированы. <br>Ваш логин: <b>{user.user_login}</b>'
                                      f'<br>Ваш пароль: <b>{password}</b>'
                                      f'<br>Запомните свои данные, так как в случае утери - восстановить их будет невозможно.'
                                      f'<br>С уважением, <b>Администрация.</b>')
                messages.success(request, message)
                logger.info('Зарегал нового')
                return redirect('cabinet')

    else:
        form = RegisterForm()

    return render(request, './auth/register.html', {'form': form})




