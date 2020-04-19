from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Print all models and object counts'

    def handle(self, *args, **options):
        models = ContentType.objects.all()
        for model in models:
            count = model.objects.all().count()
            print(f'Model: {model.model}')
            print(f'Objects count: {count}')
