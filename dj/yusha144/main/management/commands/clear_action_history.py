# main/management/commands/clear_action_history.py
from django.core.management.base import BaseCommand
from django.contrib.admin.models import LogEntry


class Command(BaseCommand):
    help = 'Удаляет все записи истории действий'

    def handle(self, *args, **kwargs):
        LogEntry.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('История действий успешно очищена'))
