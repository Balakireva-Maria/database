import csv

from django.core.management.base import BaseCommand

from work_with_database.phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                Phone.objects.create(name=line[1], price=line[2], release_date=line[4], image=line[3])
                pass
