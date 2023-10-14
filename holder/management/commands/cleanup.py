from django.core.management.base import BaseCommand
from holder.models import Cart

class Command(BaseCommand):
    help = 'Clean up Cart objects from the database'

    def handle(self, *args, **options):
        Cart.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All Cart objects were deleted'))