from django.core.management.base import BaseCommand
from subquery.models import User


class Command(BaseCommand):
    help = "trigger error"

    def handle(self, *args, **options):
        qs = User.objects.annotate_active_subscription_id()
        print(qs.query)
        print(qs.count())
