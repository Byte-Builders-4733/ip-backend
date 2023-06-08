import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from api.models import Word


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(
            os.path.join(
                settings.BASE_DIR,
                'static', 'data', 'words.csv'
            ),
            'r', encoding='utf-8'
        ) as f:
            csv_reader = csv.reader(f, delimiter=';')
            for row in csv_reader:
                Word.objects.create(term=row[1],
                                      definition=row[2], category=row[3],
                                      complexity=row[4])