# views.py
from .forms import UserRegistrationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .models import UserProfile


def home(request):
    return render(request, 'main/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            group = form.cleaned_data.get('group')
            user.groups.add(group)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('user_profile')
        else:
            # Обработка случая, если форма не валидна
            return render(request, 'main/signup.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'main/signup.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomAuthenticationForm


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 недели
                else:
                    request.session.set_expiry(0)  # Закрытие браузера
                return redirect('home')  # Замените 'home' на имя вашей главной страницы
            else:
                messages.error(request, 'Неверный ID или пароль.')
        else:
            messages.error(request, 'Неверный ID или пароль.')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'main/login.html', {'form': form})


@login_required
def user_profile(request):
    user = request.user
    if not hasattr(user, 'userprofile'):
        UserProfile.objects.create(user=user)
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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Section, Chapter
from .forms import CourseForm, SectionForm, ChapterForm
from django.contrib.auth.models import Group


@login_required
def create_course(request):
    is_teacher = request.user.groups.filter(name='Преподаватели').exists()
    if not is_teacher:
        return redirect('home')

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = CourseForm()
    return render(request, 'main/create_course.html', {'form': form, 'is_teacher': is_teacher})


@login_required
def create_section(request, course_id):
    is_teacher = request.user.groups.filter(name='Преподаватели').exists()
    if not is_teacher:
        return redirect('home')

    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.course = course
            section.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = SectionForm()
    return render(request, 'main/create_section.html', {'form': form, 'course': course, 'is_teacher': is_teacher})


@login_required
def create_chapter(request, section_id):
    is_teacher = request.user.groups.filter(name='Преподаватели').exists()
    if not is_teacher:
        return redirect('home')

    section = get_object_or_404(Section, id=section_id)
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.section = section
            chapter.save()
            return redirect('course_detail', course_id=section.course.id)
    else:
        form = ChapterForm()
    return render(request, 'main/create_chapter.html', {'form': form, 'section': section, 'is_teacher': is_teacher})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    sections = course.sections.all()
    return render(request, 'main/course_detail.html', {'course': course, 'sections': sections})


def section_detail(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    chapters = section.chapters.all()
    return render(request, 'main/section_detail.html', {'section': section, 'chapters': chapters})


def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    return render(request, 'main/chapter_detail.html', {'chapter': chapter})


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'main/courses_list.html', {'courses': courses})
