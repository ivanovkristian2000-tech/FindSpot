from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Create default user groups"

    def handle(self, *args, **options):
        groups = ["Renter", "Landlord"]

        for name in groups:
            group, created = Group.objects.get_or_create(name=name)

            if created:
                self.stdout.write(f"Group '{name}' created.")
            else:
                self.stdout.write(f"Group '{name}' already exists.")
