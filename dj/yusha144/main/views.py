# views.py
from .forms import UserRegistrationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages


def home(request):
    return render(request, 'main/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data.get('group')
            user.groups.add(group)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            # Обработка случая, если форма не валидна
            return render(request, 'main/signup.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


@login_required
def user_profile(request):
    user = request.user
    profile = user.userprofile
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email if user.email else 'Не указана',
        'date_joined': user.date_joined,
        'group': user.groups.first().name if user.groups.exists() else 'Не указана',
        'profile_picture': profile.profile_picture.url,
    }
    return render(request, 'main/user_profile.html', context)
