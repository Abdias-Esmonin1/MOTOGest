from decouple import config
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create or update the default MotoGest administrator account."

    def handle(self, *args, **options):
        username = config("ADMIN_USERNAME", default="Zadmin")
        password = config("ADMIN_PASSWORD", default="MMDR")
        email = config("ADMIN_EMAIL", default="admin@motogest.ci")

        User = get_user_model()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            },
        )

        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        action = "created" if created else "updated"
        self.stdout.write(self.style.SUCCESS(f"Admin {username} {action}."))
