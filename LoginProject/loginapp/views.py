from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def login_view(request):
    message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('success')
            else:
                message = "Invalid username or password."
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form,
        'message': message
    })


def success_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'success.html')
