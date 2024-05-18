from django.db import models


# Create your models here.
class new_users(models.Model):
    login = models.CharField('ID', max_length=20)
    first_name = models.CharField('Имя', max_length=25)
    second_name = models.CharField('Фамилия', max_length=25)
    group = models.CharField('Группа', max_length=10)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'  # ед. число
        verbose_name_plural = 'Пользователи'  # мн. число
