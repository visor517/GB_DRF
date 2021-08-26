from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Create Users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        count = options['count']
        for i in range(count):
            user = User.objects.create(username=f'user{i}', first_name=f'name{i}',
                                       last_name=f'lastname{i}', email=f'user{i}@none.net',
                                       password='geekbrains')
            print(f'user {user} created')
        print('done')
