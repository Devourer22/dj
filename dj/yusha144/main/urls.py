# main/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/sections/create/', views.create_section, name='create_section'),
    path('sections/<int:section_id>/', views.section_detail, name='section_detail'),
    path('sections/<int:section_id>/chapters/create/', views.create_chapter, name='create_chapter'),
    path('chapters/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    path('courses/', views.courses_list, name='courses'),
]
