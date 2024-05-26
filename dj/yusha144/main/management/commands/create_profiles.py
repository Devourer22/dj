from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import UserProfile


class Command(BaseCommand):
    help = 'Create user profiles for existing users'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(userprofile__isnull=True)
        for user in users_without_profiles:
            UserProfile.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS('Successfully created profiles for existing users.'))
