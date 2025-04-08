import json
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Load training data into MongoDB'

    def handle(self, *args, **options):
        db = settings.DB
        collection = db.training_data

        collection.drop()
        self.stdout.write('Cleared existing training data')

        with open('data/conversations.json', 'r') as f:
            data = json.load(f)
            collection.insert_many(data)
            self.stdout.write(self.style.SUCCESS(f'Loaded {len(data)} conversation pairs into "training_data" collection'))
