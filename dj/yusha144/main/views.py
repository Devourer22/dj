# Create your views here.
def index(request):  # страница index
    return render(request, 'main/index_main.html')


def login(request):  # страница login
    return render(request, 'main/index_login.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # при удачном входе переходим на страницу ...
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'main/index_login.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.profile.group = form.cleaned_data.get('group')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, f'Ваш аккаунт был создан, {user.username}!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'main/index_reg.html', {'form': form})
