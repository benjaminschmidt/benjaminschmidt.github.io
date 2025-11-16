from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        for user in User.objects.all():
            user.delete()
