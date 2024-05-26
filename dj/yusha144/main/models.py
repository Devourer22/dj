# main\models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class CustomUser(AbstractUser):
    additional_field = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default_profile.png')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Изменяем related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Изменяем related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username


from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default_profile.png')
    additional_field = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
