from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # при заходе на главную страницу выводим функцию index из views
    path('login/', views.login_view, name='login')  # при заходе на страницу login выводим функцию login из views
]
