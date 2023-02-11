from django.shortcuts import redirect, render
from ..handlers.forms import LoginForm
from django.contrib.auth import login
from django.contrib import messages
from ..handlers.backends import HashedPasswordAuthBackend


def log_in(request):

    if request.method == 'POST':

        if request.POST['action'] == 'Войти':
            form = LoginForm(data=request.POST)

            if form.is_valid():
                user = HashedPasswordAuthBackend().authenticate(
                    request=request,
                    user_login=form.cleaned_data['login'],
                    password=form.cleaned_data['password']
                )

                if user:
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('cabinet')

                else:
                    messages.error(request, 'Неправильный логин или пароль.')
    else:
        form = LoginForm()

    return render(request, './auth/login.html', {'form': form})