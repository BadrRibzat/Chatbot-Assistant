from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Initialize the MongoDB database for the chatbot'

    def handle(self, *args, **options):
        db = settings.DB
        # Create a messages collection if it doesn't exist
        if 'messages' not in db.list_collection_names():
            db.create_collection('messages')
            self.stdout.write(self.style.SUCCESS('Created "messages" collection'))
        else:
            self.stdout.write('Collection "messages" already exists')

        # Optionally create an index for faster queries
        db.messages.create_index('user_id')
        self.stdout.write(self.style.SUCCESS('Created index on "user_id"'))
